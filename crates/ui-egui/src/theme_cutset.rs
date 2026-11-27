//! Cutset's palette on top of the inherited themes (hoshima-ut/cutset#2).
//!
//! Only colours change: every size, radius, font and layout token stays as the inherited theme
//! sets it, so panels keep their parts, positions and hit areas. Kept in its own module so that
//! upstream changes to `theme.rs` merge without touching the palette.
//!
//! - Chrome is a graphite with a slight violet cast; panel borders sit close to the panel colour
//!   so the frame recedes behind the media.
//! - The accent is the wordmark purple (`#673B99`) lifted until white text on it and the focus
//!   outline against the panels stay readable.
//! - The playhead uses the wordmark's yamabuki yellow, so it never reads as the focus outline.
//! - The monitor surround stays neutral grey: a tinted surround would bias colour judgements.
//! - Audio, meter, plot and effect palettes are untouched, so warning and level colours keep
//!   their meaning.

use egui::Color32;

use crate::theme::Tokens;

const fn rgb(hex: u32) -> Color32 {
    Color32::from_rgb((hex >> 16) as u8, (hex >> 8) as u8, hex as u8)
}

/// The accent of every Cutset theme; `DEFAULT_HIGHLIGHT` in the engine settings names the same colour.
const ACCENT: Color32 = rgb(0x7c4dcc);
const ACCENT_HOVER: Color32 = rgb(0x8d5fdd);
const GRAPHITE: Color32 = rgb(0x17161c);

/// The darkest theme, the default.
pub fn night(base: Tokens) -> Tokens {
    Tokens {
        app_bg: rgb(0x08080b),
        header_bg: GRAPHITE,
        panel_bg: GRAPHITE,
        tab_bg: GRAPHITE,
        tab_text: rgb(0xa9a5b5),
        tab_text_active: rgb(0xf2f0f7),
        focus: rgb(0xb08cf5),
        accent: ACCENT,
        accent_hover: ACCENT_HOVER,
        text: rgb(0xe4e2ea),
        text_dim: rgb(0xb4b0c0),
        text_faint: rgb(0x9893a6),
        icon: rgb(0xa9a5b5),
        icon_active: rgb(0xf2f0f7),
        hover: rgb(0x24222c),
        pressed: rgb(0x3a3548),
        field_bg: rgb(0x0f0e14),
        field_border: rgb(0x67627a),
        separator: rgb(0x2a2833),
        row_alt: rgb(0x1b1a21),
        row_selected: rgb(0x2e2840),
        hot_text: rgb(0xc3a6ff),
        button_hover: rgb(0x2a2833),
        button_border: rgb(0x67627a),
        scroll_thumb: rgb(0x3f3b4c),
        scroll_thumb_hover: rgb(0x5a5470),
        vertical_scroll_thumb: rgb(0x4a4659),
        tl_bg: GRAPHITE,
        tl_track_bg: GRAPHITE,
        tl_track_bg_alt: rgb(0x1a1920),
        tl_header_bg: GRAPHITE,
        tl_ruler_bg: rgb(0x121117),
        tl_ruler_tick: rgb(0x8e8a9c),
        tl_ruler_text: rgb(0xb4b0c0),
        playhead: rgb(0xecaa1e),
        track_target: rgb(0x5b3a99),
        in_out_shade: rgb(0x393545),
        monitor_bg: Color32::from_gray(0x16),
        timecode: rgb(0xc3a6ff),
        ..base
    }
}

/// The lighter grey theme keeps its own surfaces and takes the Cutset highlights.
pub fn dusk(base: Tokens) -> Tokens {
    let n = night(base);
    Tokens {
        accent: n.accent,
        accent_hover: n.accent_hover,
        focus: n.focus,
        hot_text: n.hot_text,
        timecode: n.timecode,
        playhead: n.playhead,
        track_target: n.track_target,
        ..base
    }
}

/// The light theme: the wordmark purple itself reads on light panels.
pub fn daylight(base: Tokens) -> Tokens {
    let purple = rgb(0x673b99);
    Tokens {
        accent: ACCENT,
        accent_hover: ACCENT_HOVER,
        focus: purple,
        hot_text: purple,
        timecode: purple,
        track_target: rgb(0x8d5fdd),
        playhead: rgb(0x8a5a00),
        ..base
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::theme::ThemeKind;

    /// WCAG 2 contrast ratio.
    fn contrast(a: Color32, b: Color32) -> f32 {
        let lum = |c: Color32| {
            let lin = |v: u8| {
                let v = f32::from(v) / 255.0;
                if v <= 0.040_45 { v / 12.92 } else { ((v + 0.055) / 1.055).powf(2.4) }
            };
            0.2126 * lin(c.r()) + 0.7152 * lin(c.g()) + 0.0722 * lin(c.b())
        };
        let (x, y) = (lum(a), lum(b));
        (x.max(y) + 0.05) / (x.min(y) + 0.05)
    }

    fn at_least(ratio: f32, fg: Color32, bg: Color32, what: &str) {
        let got = contrast(fg, bg);
        assert!(got >= ratio, "{what}: {fg:?} on {bg:?} is {got:.2}:1, below {ratio}:1");
    }

    #[test]
    fn night_text_reads_on_every_chrome_surface() {
        let t = Tokens::for_kind(ThemeKind::Dark);
        for (name, bg) in [
            ("panel", t.panel_bg),
            ("header", t.header_bg),
            ("track", t.tl_track_bg),
            ("alternate track", t.tl_track_bg_alt),
            ("ruler", t.tl_ruler_bg),
            ("selected row", t.row_selected),
            ("hover", t.hover),
            ("field", t.field_bg),
        ] {
            for (role, fg) in [
                ("text", t.text),
                ("dim text", t.text_dim),
                ("faint text", t.text_faint),
                ("tab", t.tab_text),
                ("timecode", t.timecode),
                ("ruler text", t.tl_ruler_text),
            ] {
                at_least(4.5, fg, bg, &format!("{role} on {name}"));
            }
        }
        at_least(4.5, Color32::WHITE, t.accent, "text on the accent");
    }

    #[test]
    fn night_controls_and_focus_stand_out_from_the_panels() {
        let t = Tokens::for_kind(ThemeKind::Dark);
        for bg in [t.panel_bg, t.tab_bg, t.tl_track_bg, t.field_bg] {
            at_least(3.0, t.focus, bg, "focus outline");
            at_least(3.0, t.playhead, bg, "playhead");
        }
        at_least(3.0, t.field_border, t.panel_bg, "field outline");
        at_least(3.0, t.field_border, t.field_bg, "field outline inside");
        // The frame recedes: panel dividers are quieter than control outlines.
        assert!(contrast(t.separator, t.panel_bg) < contrast(t.field_border, t.panel_bg));
    }

    #[test]
    fn the_playhead_and_focus_are_told_apart_by_hue() {
        let hue = |c: Color32| egui::ecolor::HsvaGamma::from(c).h;
        for kind in [ThemeKind::Dark, ThemeKind::Medium, ThemeKind::Light] {
            let t = Tokens::for_kind(kind);
            let apart = (hue(t.playhead) - hue(t.focus)).abs();
            assert!(apart.min(1.0 - apart) > 0.2, "{kind:?}: playhead and focus share a hue");
        }
    }

    #[test]
    fn the_monitor_surround_stays_neutral() {
        for kind in [ThemeKind::Dark, ThemeKind::Medium, ThemeKind::Light] {
            let c = Tokens::for_kind(kind).monitor_bg;
            assert!(c.r() == c.g() && c.g() == c.b(), "{kind:?}: tinted monitor surround {c:?}");
        }
    }

    #[test]
    fn every_theme_uses_the_default_highlight_as_its_accent() {
        let default = filmcraft_engine::settings::parse_hex(filmcraft_engine::settings::DEFAULT_HIGHLIGHT);
        for kind in [ThemeKind::Dark, ThemeKind::Medium, ThemeKind::Light] {
            let t = Tokens::for_kind(kind);
            assert_eq!(default.map(|[r, g, b]| Color32::from_rgb(r, g, b)), Some(t.accent), "{kind:?}");
        }
    }

    #[test]
    fn light_theme_highlights_read_on_light_panels() {
        let t = Tokens::for_kind(ThemeKind::Light);
        at_least(3.0, t.focus, t.panel_bg, "focus outline");
        at_least(3.0, t.playhead, t.tl_track_bg, "playhead");
        at_least(4.5, t.timecode, t.panel_bg, "timecode");
        at_least(4.5, Color32::WHITE, t.accent, "text on the accent");
    }

    #[test]
    fn sizes_and_shapes_are_inherited_unchanged() {
        for kind in [ThemeKind::Dark, ThemeKind::Medium, ThemeKind::Light] {
            let t = Tokens::for_kind(kind);
            let base = Tokens::inherited(kind);
            assert_eq!((t.radius, t.radius_sm, t.gap, t.tab_h), (base.radius, base.radius_sm, base.gap, base.tab_h), "{kind:?}");
        }
    }
}
