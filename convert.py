"""vim-color-spring-night を VSCode テーマ拡張に変換するスクリプト"""

import json
import os

# パレット（palette.rs から抽出）
PALETTE = {
    "bg":         "#334152",
    "bg_hc":      "#132132",
    "bgweaker":   "#3a4b5c",
    "bgweaker_hc":"#213243",
    "bgemphasis": "#3a4b5c",
    "bglight":    "#435060",
    "bgstrong":   "#536273",
    "light":      "#646f7c",
    "fg":         "#fffeeb",
    "hiddenfg":   "#607080",
    "weakfg":     "#8d9eb2",
    "weakerfg":   "#788898",
    "green":      "#a9dd9d",
    "skyblue":    "#a8d2eb",
    "yellow":     "#f0eaaa",
    "gold":       "#fedf81",
    "orange":     "#f0aa8a",
    "red":        "#fd8489",
    "purple":     "#e7d5ff",
    "palepink":   "#e7c6b7",
    "mikan":      "#fb8965",
    "nasu":       "#605779",
    "yaezakura":  "#70495d",
    "sakura":     "#a9667a",
    "mildred":    "#ab6560",
    "darkgreen":  "#5f8770",
    "darkgold":   "#685800",
    "crimson":    "#ff6a6f",
    "lime":       "#c9fd88",
    "blue":       "#7098e6",
    "paleblue":   "#98b8e6",
    "sunny":      "#b8e2fb",
    "fuchsia":    "#b9a5cf",
}

# vim highlight group -> VSCode editor colors のマッピング
EDITOR_COLORS = {
    # エディタ基本
    "editor.background":                    PALETTE["bg"],
    "editor.foreground":                    PALETTE["fg"],
    "editor.lineHighlightBackground":       PALETTE["bgweaker"] + "80",
    "editorLineNumber.foreground":          PALETTE["weakerfg"],
    "editorLineNumber.activeForeground":    PALETTE["purple"],
    "editorCursor.foreground":              PALETTE["fg"],
    "editor.selectionBackground":           PALETTE["yaezakura"] + "99",
    "editor.selectionHighlightBackground":  PALETTE["yaezakura"] + "55",
    "editor.wordHighlightBackground":       PALETTE["nasu"] + "55",
    "editor.wordHighlightStrongBackground": PALETTE["nasu"] + "88",

    # 検索
    "editor.findMatchBackground":           PALETTE["sakura"] + "99",
    "editor.findMatchHighlightBackground":  PALETTE["nasu"] + "99",
    "editor.rangeHighlightBackground":      PALETTE["bgweaker"] + "66",

    # ブラケット
    "editorBracketMatch.background":        PALETTE["gold"] + "30",
    "editorBracketMatch.border":            PALETTE["gold"],
    # ブラケットペアカラー（Vimのfgに統一）
    "editorBracketHighlight.foreground1":   PALETTE["fg"],
    "editorBracketHighlight.foreground2":   PALETTE["fg"],
    "editorBracketHighlight.foreground3":   PALETTE["fg"],
    "editorBracketHighlight.foreground4":   PALETTE["fg"],
    "editorBracketHighlight.foreground5":   PALETTE["fg"],
    "editorBracketHighlight.foreground6":   PALETTE["fg"],
    "editorBracketHighlight.unexpectedBracket.foreground": PALETTE["red"],

    # インデントガイド
    "editorIndentGuide.background":         PALETTE["bgweaker"],
    "editorIndentGuide.activeBackground":   PALETTE["bgstrong"],

    # エラー・警告
    "editorError.foreground":               PALETTE["red"],
    "editorWarning.foreground":             PALETTE["orange"],
    "editorInfo.foreground":                PALETTE["skyblue"],

    # ルーラー・オーバービュー
    "editorRuler.foreground":               PALETTE["bgstrong"],
    "editorOverviewRuler.border":           PALETTE["bgstrong"],
    "editorOverviewRuler.errorForeground":  PALETTE["red"],
    "editorOverviewRuler.warningForeground":PALETTE["orange"],
    "editorOverviewRuler.findMatchForeground": PALETTE["sakura"],

    # ホワイトスペース
    "editorWhitespace.foreground":          PALETTE["light"],
    "editorCodeLens.foreground":            PALETTE["weakfg"],

    # diff
    "diffEditor.insertedTextBackground":    PALETTE["darkgreen"] + "44",
    "diffEditor.removedTextBackground":     PALETTE["mildred"] + "44",
    "diffEditor.insertedLineBackground":    PALETTE["darkgreen"] + "22",
    "diffEditor.removedLineBackground":     PALETTE["mildred"] + "22",

    # タブ・エディタグループ
    "editorGroupHeader.tabsBackground":     PALETTE["bg"],
    "tab.activeBackground":                 PALETTE["bg"],
    "tab.activeForeground":                 PALETTE["fg"],
    "tab.inactiveBackground":               PALETTE["bgweaker"],
    "tab.inactiveForeground":               PALETTE["weakfg"],
    "tab.border":                           PALETTE["bg"],
    "tab.activeBorderTop":                  PALETTE["gold"],

    # サイドバー
    "sideBar.background":                   PALETTE["bg"],
    "sideBar.foreground":                   PALETTE["fg"],
    "sideBar.border":                       PALETTE["bgweaker"],
    "sideBarTitle.foreground":              PALETTE["weakfg"],
    "sideBarSectionHeader.background":      PALETTE["bgweaker"],
    "sideBarSectionHeader.foreground":      PALETTE["fg"],

    # アクティビティバー
    "activityBar.background":               PALETTE["bg"],
    "activityBar.foreground":               PALETTE["fg"],
    "activityBar.border":                   PALETTE["bgweaker"],
    "activityBarBadge.background":          PALETTE["gold"],
    "activityBarBadge.foreground":          PALETTE["bg_hc"],

    # ステータスバー（StatusLine から）
    "statusBar.background":                 PALETTE["bgstrong"],
    "statusBar.foreground":                 PALETTE["fg"],
    "statusBar.border":                     PALETTE["bgstrong"],
    "statusBar.noFolderBackground":         PALETTE["bgstrong"],
    "statusBarItem.hoverBackground":        PALETTE["bgweaker"],

    # タイトルバー
    "titleBar.activeBackground":            PALETTE["bg"],
    "titleBar.activeForeground":            PALETTE["fg"],
    "titleBar.inactiveBackground":          PALETTE["bg"],
    "titleBar.inactiveForeground":          PALETTE["weakfg"],

    # パネル（ターミナルなど）
    "panel.background":                     PALETTE["bg"],
    "panel.border":                         PALETTE["bgweaker"],
    "panelTitle.activeForeground":          PALETTE["gold"],
    "panelTitle.activeBorder":              PALETTE["gold"],
    "panelTitle.inactiveForeground":        PALETTE["weakfg"],

    # ポップアップ・補完（Pmenu から）
    "editorSuggestWidget.background":       PALETTE["bgweaker"],
    "editorSuggestWidget.border":           PALETTE["bgstrong"],
    "editorSuggestWidget.foreground":       PALETTE["purple"],
    "editorSuggestWidget.selectedBackground":PALETTE["bgstrong"],
    "editorSuggestWidget.highlightForeground": PALETTE["gold"],
    "editorWidget.background":              PALETTE["bgweaker"],
    "editorWidget.border":                  PALETTE["bgstrong"],

    # ホバー
    "editorHoverWidget.background":         PALETTE["bgweaker"],
    "editorHoverWidget.border":             PALETTE["bgstrong"],

    # ピーク表示
    "peekView.border":                      PALETTE["skyblue"],
    "peekViewEditor.background":            PALETTE["bg"],
    "peekViewEditor.matchHighlightBackground": PALETTE["nasu"] + "88",
    "peekViewResult.background":            PALETTE["bgweaker"],
    "peekViewResult.matchHighlightBackground": PALETTE["nasu"] + "88",
    "peekViewTitle.background":             PALETTE["bgweaker"],
    "peekViewTitleLabel.foreground":        PALETTE["fg"],
    "peekViewTitleDescription.foreground":  PALETTE["weakfg"],

    # 入力
    "input.background":                     PALETTE["bgweaker"],
    "input.foreground":                     PALETTE["fg"],
    "input.border":                         PALETTE["bgstrong"],
    "input.placeholderForeground":          PALETTE["weakfg"],
    "inputOption.activeBorder":             PALETTE["gold"],

    # ドロップダウン
    "dropdown.background":                  PALETTE["bgweaker"],
    "dropdown.foreground":                  PALETTE["fg"],
    "dropdown.border":                      PALETTE["bgstrong"],

    # ボタン
    "button.background":                    PALETTE["blue"],
    "button.foreground":                    PALETTE["fg"],
    "button.hoverBackground":               PALETTE["skyblue"],

    # スクロールバー
    "scrollbar.shadow":                     "#00000044",
    "scrollbarSlider.background":           PALETTE["bgstrong"] + "88",
    "scrollbarSlider.hoverBackground":      PALETTE["bgstrong"] + "bb",
    "scrollbarSlider.activeBackground":     PALETTE["bgstrong"],

    # ミニマップ
    "minimap.findMatchHighlight":           PALETTE["sakura"],
    "minimap.selectionHighlight":           PALETTE["yaezakura"],
    "minimap.errorHighlight":               PALETTE["red"],
    "minimap.warningHighlight":             PALETTE["orange"],
    "minimapGutter.addedBackground":        PALETTE["darkgreen"],
    "minimapGutter.modifiedBackground":     PALETTE["darkgold"],
    "minimapGutter.deletedBackground":      PALETTE["mildred"],

    # git 装飾（GitGutter/Signify から）
    "gitDecoration.addedResourceForeground":        PALETTE["green"],
    "gitDecoration.modifiedResourceForeground":     PALETTE["yellow"],
    "gitDecoration.deletedResourceForeground":      PALETTE["red"],
    "gitDecoration.untrackedResourceForeground":    PALETTE["green"],
    "gitDecoration.ignoredResourceForeground":      PALETTE["light"],
    "gitDecoration.conflictingResourceForeground":  PALETTE["mikan"],

    # ノーティフィケーション
    "notificationCenterHeader.background":  PALETTE["bgweaker"],
    "notifications.background":             PALETTE["bgweaker"],
    "notifications.border":                 PALETTE["bgstrong"],

    # リスト・ツリー
    "list.activeSelectionBackground":       PALETTE["bgstrong"],
    "list.activeSelectionForeground":       PALETTE["fg"],
    "list.inactiveSelectionBackground":     PALETTE["bgweaker"],
    "list.hoverBackground":                 PALETTE["bgweaker"],
    "list.hoverForeground":                 PALETTE["fg"],
    "list.focusBackground":                 PALETTE["bgstrong"],
    "list.highlightForeground":             PALETTE["gold"],
    "list.errorForeground":                 PALETTE["red"],
    "list.warningForeground":               PALETTE["orange"],

    # ターミナル
    "terminal.background":                  PALETTE["bg"],
    "terminal.foreground":                  PALETTE["fg"],
    "terminal.ansiBlack":                   PALETTE["bg_hc"],
    "terminal.ansiRed":                     PALETTE["crimson"],
    "terminal.ansiGreen":                   PALETTE["green"],
    "terminal.ansiYellow":                  PALETTE["gold"],
    "terminal.ansiBlue":                    PALETTE["blue"],
    "terminal.ansiMagenta":                 PALETTE["purple"],
    "terminal.ansiCyan":                    PALETTE["skyblue"],
    "terminal.ansiWhite":                   PALETTE["fg"],
    "terminal.ansiBrightBlack":             PALETTE["weakerfg"],
    "terminal.ansiBrightRed":               PALETTE["red"],
    "terminal.ansiBrightGreen":             PALETTE["lime"],
    "terminal.ansiBrightYellow":            PALETTE["yellow"],
    "terminal.ansiBrightBlue":              PALETTE["paleblue"],
    "terminal.ansiBrightMagenta":           PALETTE["purple"],
    "terminal.ansiBrightCyan":              PALETTE["sunny"],
    "terminal.ansiBrightWhite":             "#ffffff",
    "terminal.selectionBackground":         PALETTE["yaezakura"] + "99",

    # フォーカスボーダー
    "focusBorder":                          PALETTE["gold"] + "88",

    # 選択ハイライト
    "selection.background":                 PALETTE["yaezakura"],
}

# TextMate スコープ（tokenColors）
TOKEN_COLORS = [
    {
        "name": "Comment",
        "scope": ["comment", "punctuation.definition.comment"],
        "settings": {"foreground": PALETTE["weakfg"], "fontStyle": "italic"},
    },
    {
        "name": "String",
        "scope": [
            "string",
            "string.quoted",
            "string.template",
        ],
        "settings": {"foreground": PALETTE["green"]},
    },
    {
        "name": "String escape / special char",
        "scope": ["constant.character.escape", "string.regexp"],
        "settings": {"foreground": PALETTE["skyblue"]},
    },
    {
        "name": "Number / Boolean / Null",
        "scope": [
            "constant.numeric",
            "constant.language",
            "constant.character",
        ],
        "settings": {"foreground": PALETTE["red"]},
    },
    {
        "name": "Constant (other)",
        "scope": ["constant"],
        "settings": {"foreground": PALETTE["red"]},
    },
    {
        "name": "Keyword",
        "scope": [
            "keyword",
            "keyword.control",
            "keyword.other",
            "storage.modifier",
        ],
        "settings": {"foreground": PALETTE["yellow"], "fontStyle": "bold"},
    },
    {
        "name": "Operator",
        "scope": ["keyword.operator"],
        "settings": {"foreground": PALETTE["orange"]},
    },
    {
        "name": "Statement / control flow",
        "scope": [
            "keyword.control.conditional",
            "keyword.control.loop",
            "keyword.control.return",
            "keyword.control.import",
            "keyword.control.flow",
            "storage.type.function",
            "storage.type.class",
            "keyword.declaration.function",
            "keyword.declaration.class",
        ],
        "settings": {"foreground": PALETTE["skyblue"]},
    },
    {
        "name": "Function definition",
        "scope": [
            "entity.name.function",
            "meta.function entity.name.function",
            "support.function",
        ],
        "settings": {"foreground": PALETTE["orange"]},
    },
    {
        "name": "Function call",
        "scope": [
            "meta.function-call entity.name.function",
            "meta.method-call entity.name.function",
        ],
        "settings": {"foreground": PALETTE["orange"]},
    },
    {
        "name": "Type / Class",
        "scope": [
            "entity.name.type",
            "entity.name.class",
            "entity.name.struct",
            "entity.name.enum",
            "support.class",
            "support.type",
        ],
        "settings": {"foreground": PALETTE["gold"]},
    },
    {
        "name": "Storage type",
        "scope": ["storage.type"],
        "settings": {"foreground": PALETTE["gold"], "fontStyle": "italic"},
    },
    {
        "name": "Variable / Identifier",
        "scope": [
            "variable",
            "variable.other",
            "meta.definition.variable",
        ],
        "settings": {"foreground": PALETTE["fg"]},
    },
    {
        "name": "Constant name (readonly variable)",
        "scope": [
            "variable.other.constant",
            "variable.other.enummember",
            "constant.other",
        ],
        "settings": {"foreground": PALETTE["fg"]},
    },
    {
        "name": "Variable parameter",
        "scope": [
            "variable.parameter",
            "meta.function.parameters variable",
        ],
        "settings": {"foreground": PALETTE["fg"]},
    },
    {
        "name": "Property / Member",
        "scope": [
            "variable.other.property",
            "variable.other.object.property",
            "support.variable.property",
            "meta.object.member",
        ],
        "settings": {"foreground": PALETTE["fg"]},
    },
    {
        "name": "Namespace / Module",
        "scope": [
            "entity.name.namespace",
            "entity.name.module",
            "support.module",
        ],
        "settings": {"foreground": PALETTE["yellow"]},
    },
    {
        "name": "Preprocessor / Macro",
        "scope": [
            "meta.preprocessor",
            "keyword.control.directive",
            "entity.name.function.preprocessor",
            "keyword.other.special-method",
        ],
        "settings": {"foreground": PALETTE["orange"]},
    },
    {
        "name": "Label",
        "scope": ["entity.name.label"],
        "settings": {"foreground": PALETTE["skyblue"]},
    },
    {
        "name": "Tag (HTML/XML)",
        "scope": [
            "entity.name.tag",
            "meta.tag",
        ],
        "settings": {"foreground": PALETTE["orange"]},
    },
    {
        "name": "Tag attribute",
        "scope": [
            "entity.other.attribute-name",
        ],
        "settings": {"foreground": PALETTE["yellow"]},
    },
    {
        "name": "Tag punctuation",
        "scope": [
            "punctuation.definition.tag",
        ],
        "settings": {"foreground": PALETTE["weakfg"]},
    },
    {
        "name": "CSS property name",
        "scope": [
            "support.type.property-name",
            "meta.property-name",
        ],
        "settings": {"foreground": PALETTE["skyblue"]},
    },
    {
        "name": "CSS property value",
        "scope": [
            "support.constant.property-value",
            "meta.property-value",
        ],
        "settings": {"foreground": PALETTE["orange"]},
    },
    {
        "name": "CSS selector",
        "scope": [
            "entity.name.tag.css",
            "entity.other.attribute-name.class.css",
            "entity.other.attribute-name.id.css",
        ],
        "settings": {"foreground": PALETTE["yellow"]},
    },
    {
        "name": "Invalid / Error",
        "scope": ["invalid"],
        "settings": {"foreground": PALETTE["red"], "fontStyle": "bold"},
    },
    {
        "name": "Special / punctuation",
        "scope": [
            "punctuation",
            "punctuation.separator",
            "punctuation.terminator",
        ],
        "settings": {"foreground": PALETTE["fg"]},
    },
    {
        "name": "Markdown heading",
        "scope": ["markup.heading", "entity.name.section"],
        "settings": {"foreground": PALETTE["gold"], "fontStyle": "bold"},
    },
    {
        "name": "Markdown bold",
        "scope": ["markup.bold"],
        "settings": {"foreground": PALETTE["fg"], "fontStyle": "bold"},
    },
    {
        "name": "Markdown italic",
        "scope": ["markup.italic"],
        "settings": {"foreground": PALETTE["fg"], "fontStyle": "italic"},
    },
    {
        "name": "Markdown code",
        "scope": ["markup.inline.raw", "markup.fenced_code.block"],
        "settings": {"foreground": PALETTE["yellow"]},
    },
    {
        "name": "Markdown link",
        "scope": ["markup.underline.link"],
        "settings": {"foreground": PALETTE["skyblue"]},
    },
    {
        "name": "Markdown list bullet",
        "scope": ["punctuation.definition.list_item"],
        "settings": {"foreground": PALETTE["orange"]},
    },
    {
        "name": "Diff added",
        "scope": ["markup.inserted"],
        "settings": {"foreground": PALETTE["green"]},
    },
    {
        "name": "Diff removed",
        "scope": ["markup.deleted"],
        "settings": {"foreground": PALETTE["red"]},
    },
    {
        "name": "Diff changed",
        "scope": ["markup.changed"],
        "settings": {"foreground": PALETTE["yellow"]},
    },
    {
        "name": "Todo keyword",
        "scope": ["keyword.other.todo", "comment.line.note"],
        "settings": {
            "foreground": PALETTE["bg_hc"],
            "background": PALETTE["red"],
            "fontStyle": "bold",
        },
    },
    # 言語別: Python
    {
        "name": "Python builtin",
        "scope": ["support.function.builtin.python"],
        "settings": {"foreground": PALETTE["red"]},
    },
    # 言語別: Go
    {
        "name": "Go builtin",
        "scope": ["support.function.builtin.go"],
        "settings": {"foreground": PALETTE["red"]},
    },
    # 言語別: Rust enum variant
    {
        "name": "Rust enum variant",
        "scope": ["support.constant.rust"],
        "settings": {"foreground": PALETTE["gold"]},
    },
    # 言語別: TypeScript/JavaScript
    {
        "name": "TypeScript async keyword",
        "scope": ["storage.modifier.async"],
        "settings": {"foreground": PALETTE["skyblue"]},
    },
]

# セマンティックトークン（LSP ベースの追加ハイライト）
SEMANTIC_TOKEN_COLORS = {
    "variable":             {"foreground": PALETTE["fg"]},
    "variable.readonly":    {"foreground": PALETTE["fg"]},
    "parameter":            {"foreground": PALETTE["fg"]},
    "function":             {"foreground": PALETTE["orange"]},
    "method":               {"foreground": PALETTE["orange"]},
    "class":                {"foreground": PALETTE["gold"]},
    "interface":            {"foreground": PALETTE["gold"]},
    "struct":               {"foreground": PALETTE["gold"]},
    "enum":                 {"foreground": PALETTE["gold"]},
    "enumMember":           {"foreground": PALETTE["red"]},
    "namespace":            {"foreground": PALETTE["yellow"]},
    "type":                 {"foreground": PALETTE["gold"]},
    "typeParameter":        {"foreground": PALETTE["gold"], "fontStyle": "italic"},
    "property":             {"foreground": PALETTE["fg"]},
    "keyword":              {"foreground": PALETTE["yellow"], "fontStyle": "bold"},
    "string":               {"foreground": PALETTE["green"]},
    "number":               {"foreground": PALETTE["red"]},
    "comment":              {"foreground": PALETTE["weakfg"], "fontStyle": "italic"},
    "macro":                {"foreground": PALETTE["orange"]},
    "decorator":            {"foreground": PALETTE["yellow"]},
}


def build_theme() -> dict:
    return {
        "name": "Spring Night",
        "type": "dark",
        "colors": EDITOR_COLORS,
        "tokenColors": TOKEN_COLORS,
        "semanticHighlighting": False,
    }


def build_package_json(theme_filename: str) -> dict:
    return {
        "name": "vscode-spring-night",
        "displayName": "Spring Night",
        "description": "Calm-colored dark color scheme for VSCode, ported from vim-color-spring-night",
        "version": "1.0.0",
        "publisher": "spring-night",
        "license": "MIT",
        "engines": {"vscode": "^1.70.0"},
        "categories": ["Themes"],
        "keywords": ["theme", "color-theme", "dark", "spring-night"],
        "repository": {
            "type": "git",
            "url": "https://github.com/rhysd/vim-color-spring-night",
        },
        "contributes": {
            "themes": [
                {
                    "label": "Spring Night",
                    "uiTheme": "vs-dark",
                    "path": f"./themes/{theme_filename}",
                }
            ]
        },
    }


def main():
    out_dir = "vscode-spring-night"
    themes_dir = os.path.join(out_dir, "themes")
    theme_filename = "spring-night-color-theme.json"

    os.makedirs(themes_dir, exist_ok=True)

    theme_path = os.path.join(themes_dir, theme_filename)
    with open(theme_path, "w", encoding="utf-8") as f:
        json.dump(build_theme(), f, indent=2, ensure_ascii=False)
    print(f"生成: {theme_path}")

    pkg_path = os.path.join(out_dir, "package.json")
    with open(pkg_path, "w", encoding="utf-8") as f:
        json.dump(build_package_json(theme_filename), f, indent=2, ensure_ascii=False)
    print(f"生成: {pkg_path}")

    print("\n完了。VSCode で確認するには:")
    print(f"  1. VSCode で {out_dir}/ フォルダを開く")
    print("  2. F5 キー（拡張機能デバッグ）または Ctrl+Shift+P → 'Install Extension from VSIX'")
    print("  3. またはフォルダを ~/.vscode/extensions/ にコピーして再起動")


if __name__ == "__main__":
    main()
