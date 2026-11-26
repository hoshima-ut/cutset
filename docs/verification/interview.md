# 日本語インタビュー編集の試作を始める

この作業ブランチでは、FilmCraftを土台に、編集者が音を聞いて間を残すか詰めるか選べる体験を試す。基準は `v0.20.1`（`cedf0c9bd060eb06a977d532402be2097c9ebe42`）。最初の比較は上流版の手編集、固定候補の試聴、ローカル推論の順に進める。

## Macで基準版を動かす

Xcode Command Line ToolsとRust stable 1.95以上を用意し、リポジトリのルートで実行する。時間計算のテスト、CLI、デスクトップの順に確かめる。[開発環境](../development/rust.md)

```sh
cargo test --locked -p filmcraft-time
cargo build --locked --release -p filmcraft-cli -p filmcraft
mkdir -p target/first-run
./target/release/filmcraft-cli render --demo --seconds 3 --out target/first-run/frame.png
./target/release/filmcraft --demo --data-dir "$PWD/target/first-run/profile"
```

ローカルで用意した試験案件 `target/first-run/interview-64s.fcproj` がある場合は、リポジトリのルートで次を実行する。初期配置は、会話A1・A2とリンクした映像2本、ロックした音楽A3、日本語字幕C1。タイムラインの切替は44秒。試験ごとに「別名で保存」して基準案件を保管する。別の端末では下の生成手順から同じ条件を作れる。

```sh
./target/release/filmcraft target/first-run/interview-64s.fcproj --data-dir "$PWD/target/first-run/profile"
```

## 開発する順番

1. **手編集を観察する。** 下の自作素材で25 fpsのシーケンスを作り、64秒から60秒へ短縮する。音楽をロックし、素材の元フレーム [205,245) と [505,565) を詰め、[800,825) の一呼吸を残す。字幕を「高橋選手」から「髙橋選手」に直し、保存・再開・書き出しまで通す。完成尺1,500フレーム、残した呼吸 [700,725)、字幕 [1150,1200) を確認する。
2. **固定候補を試聴する。** `crates/ui-egui` のタイムラインに候補を出し、原音／変更案を同じ位置から再生する。「残す」「詰める」「戻る」をキーだけで選べるようにし、字幕のIME入力中にキーを奪わない。
3. **編集を一度で確定する。** `crates/engine` と `crates/edit` に共通の確定操作を置く。対象の版・ロック・配置IDを照合する。途中失敗、二重適用、Undo一回での全復元を検証してから、候補の供給元をローカル音声解析に差し替える。MCPの `command_batch` は逐次実行のため、呼び出しただけでは一括確定を保証しない。[既存の編集命令](../reference/filmcraft/agents.md)
4. **編集者が採否を決める。** 手動とAI支援で所要時間、迷った操作、意図しない変更、直す手数を同じ表に記録する。最後は日本語の生声で残した呼吸を聞き、次の案件でも使いたいかを尋ねる。次の段階で同じ案件をOTIO・SRTで引き渡し、ブラウザのレビューへ進む。[Web版の開発手順](../reference/filmcraft/web.md)

| 実施日・担当 | 素材／版／マシン | 手動・固定候補・推論 | 所要時間／復旧の手数 | 尺・呼吸・字幕・音楽 | 次に直す操作 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## macOSで64秒の回帰試験素材を生成する

FFmpegとffprobeが使えるターミナルで次を実行する。新しい一時ディレクトリの中に、ショット2本、ロック用の音楽、編集用のUTF-8字幕を生成する。映像はフォントを使わず原時刻を100分の1秒単位で焼き込む。カウンタは4進むごとに素材が1フレーム進む。ショット1は通常色と440 Hz、ショット2は反転色と880 Hzで識別する。どちらにもA・B・Cの無音が入る。これは編集命令の回帰試験用。日本語文字起こしの精度、子音や息の切れ、間の自然さは同じ台本を別録りした生声で編集者が確認する。[FFmpegの映像・音声生成フィルター](https://ffmpeg.org/ffmpeg-filters.html#testsrc)

```sh
fixture_dir=$(mktemp -d)
cd "$fixture_dir" || exit 1
pwd
gaps='between(n,8*48000,10*48000-1)+between(n,20*48000,23*48000-1)+between(n,32*48000,33*48000-1)'
for shot in 1 2; do
  hz=440
  video_filter='format=yuv420p'
  if [ "$shot" = 2 ]; then
    hz=880
    video_filter='negate,format=yuv420p'
  fi
  ffmpeg -v error -f lavfi -i 'testsrc=size=320x180:rate=25:duration=64:decimals=2' \
    -f lavfi -i "aevalsrc=exprs='0.1*sin(2*PI*$hz*t)*not($gaps)':s=48000:d=64" \
    -vf "$video_filter" -c:v libx264 -c:a pcm_s16le "shot-$shot.mov" || exit 1
done
ffmpeg -v error -f lavfi \
  -i "aevalsrc=exprs='0.02*sin(2*PI*110*t)+0.4*sin(2*PI*1200*t)*between(n,192000,193919)':s=48000:d=60" \
  -c:a pcm_s16le music.wav
cat > captions.srt <<'SRT'
1
00:00:50,000 --> 00:00:52,000
高橋選手
SRT
shasum -a 256 shot-1.mov shot-2.mov music.wav captions.srt > SHA256SUMS
ffprobe -v error -show_entries stream=index,codec_name,r_frame_rate,nb_frames,sample_rate,duration \
  -of compact shot-1.mov
```

1. 新規25 fpsシーケンスで、ショット1の素材区間 [0,1100) を先頭に、ショット2の [1100,1600) を直後に並べる。両方とも元の64秒ファイルを保持する。後のショットの音声を別トラックに置けば、先頭音を3フレーム前に延ばして880 Hzの入りを独立して確認できる。
2. 音楽を位置0に置き、トラックをロックする。4秒位置の1フレームだけに高い確認音が重なる。字幕を位置0基準で取り込み、会話のリップル編集に追従するトラックまたは配置にする。字幕トラックが追従しない場合は、その差を評価票に記録する。
3. ffprobeで各ショットの映像が25/1 fps、1,600フレーム、64秒、音声が48,000 Hzであることを確認する。字幕の修正後は、テキストとして「髙」（U+9AD9）が保存され、出力画面にも日本語表示用のフォントで表示されるかを別々に確認する。フォントがその字形を持たない端末は字体の目視を「未確認」とする。

この生成例はmacOSのFFmpeg 9.0.2で実行済み。両MOVの映像が各1,600フレーム、音声が各3,072,000サンプルであること、3つの無音区間、Jカットに使う3フレーム分の信号、音楽の高音の位置と長さ、字幕の原文、4ファイルのハッシュ照合を確認した。FilmCraft v0.20.1のCLIでも25 fpsの案件を作り、映像2本・音楽・字幕を取り込み、指定の初期配置を保存した。別プロセスで1,600フレーム、映像と会話のリンク、音楽のロック、日本語字幕を照合し、45秒時点を描画した。編集者による60秒化と操作性の評価は未実施。
