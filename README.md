# Spring Night for VS Code

A dark VS Code color theme ported from [vim-color-spring-night](https://github.com/rhysd/vim-color-spring-night) by [@rhysd](https://github.com/rhysd).

Deep blue backgrounds with shiny yellow foreground and sakura text selection.

## Features

- Deep blue backgrounds faithful to the original Vim theme
- Bracket pair colorization unified to foreground color
- Semantic highlighting disabled for consistent rendering regardless of language server state
- Adjusted to match Vim behavior: constant names, variables, and brackets in foreground color

## Color Palette

| Role | Color | Usage |
|------|-------|-------|
| Background | `#334152` | Editor, sidebar |
| Chrome | `#132132` | Status bar, dropdowns |
| Foreground | `#fffeeb` | Normal text (cream) |
| Comment | `#8d9eb2` | Comments |
| String | `#a9dd9d` | String literals |
| Keyword | `#f0eaaa` | Keywords |
| Control flow | `#a8d2eb` | `if`, `for`, `def`, `fn` |
| Function | `#f0aa8a` | Function names |
| Type | `#fedf81` | Types, classes |
| Number | `#fd8489` | Numeric literals |
| Selection | `#a9667a` | Text selection (sakura) |
| Status bar | `#536273` | `bgstrong` |

## Installation

### From source

```bash
git clone https://github.com/ryokn/spring-night
cp -r spring-night/vscode-spring-night ~/.vscode/extensions/spring-night-1.0.0
```

Reload VS Code: `Ctrl+Shift+P` → `Developer: Reload Window`

Then select the theme: `Ctrl+Shift+P` → `Preferences: Color Theme` → **Spring Night**

## Customization

Colors are managed in `convert.py`. Edit the `PALETTE` or `EDITOR_COLORS` / `TOKEN_COLORS` sections, then regenerate:

```bash
python convert.py
rm -rf ~/.vscode/extensions/spring-night-1.0.0
cp -r vscode-spring-night ~/.vscode/extensions/spring-night-1.0.0
```

To inspect any token's scope in VS Code: `Ctrl+Shift+P` → `Developer: Inspect Editor Tokens and Scopes`

## Credits

Based on [vim-color-spring-night](https://github.com/rhysd/vim-color-spring-night) by [@rhysd](https://github.com/rhysd).

## License

MIT — includes original copyright notice from vim-color-spring-night (© 2016 rhysd).
