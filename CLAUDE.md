# RAPIID — CLAUDE.md

Windows desktop app that images natural-history specimen labels with webcams
and FLIR cameras, decodes DataMatrix/QR/1D barcodes, and writes capture
metadata to CSV and EXIF. Ships to end users as an Inno Setup installer.

## WHAT

### Stack
- **Python 3.8 only.** The Spinnaker wheel is cp38, so no 3.9+ syntax
  (`list[int]`, `X | Y` unions, `match`, `str.removeprefix`).
- PyQt5 GUI, OpenCV (webcams, QR, 1D barcodes), pylibdmtx (DataMatrix),
  PySpin / Spinnaker SDK (FLIR), Pillow + piexif (EXIF), qt-material (theme).
- cx_Freeze builds the frozen exe; Inno Setup 7 builds the installer.
- **Interpreter:** the `python.exe` of the project's conda env. Paths for
  this machine are in `CLAUDE.local.md` (gitignored) when present.
  `environment.yml` lists direct dependencies only, pinned.
- **Pinned:** `qt-material==2.12`. Newer versions drop PyQt5 and fail to theme
  without raising an error. Don't upgrade it.

### Layout
| Path | Purpose |
|---|---|
| `rapiid.py` | The whole app (~2.5k lines): cameras, decoding, capture, UI wiring |
| `GUI/rapiid_GUI.ui` | Qt Designer layout, the source of truth for the UI |
| `GUI/rapiid_GUI.py` | **Generated** from the `.ui`. Never hand-edit |
| `GUI/pyuic5_conversion.py` | The regenerate command (comment, not a script) |
| `scripts/ymlRW.py` | YAML config read/write, optional import |
| `scripts/rapiid_FLIR.py` | Legacy and unused by `rapiid.py`. Don't build on it |
| `config.yaml` | Default config bundled into the build |
| `setup.py` | cx_Freeze build config |
| `RAPIID.iss` | Inno Setup installer script |
| `CHANGELOG.md` | User-facing release notes |
| `info/` | End-user workflow instructions (docx) |
| `ms/`, `build/`, `dist/` | Manuscript, build output, installers. Untracked; leave alone |

Key classes in `rapiid.py`: `UI` (main window), `LabelCameraSlot` (one per
label camera; each owns its own `FLIRCamera`), `FLIRCamera`, `Worker` /
`WorkerSignals` (QThreadPool), `ExifManager`, `FileManager`.

### Commands
Run from the repo root. `$PY` is the interpreter above.
```bash
# Syntax check (the minimum after any edit)
$PY -c "import ast; ast.parse(open('rapiid.py',encoding='utf-8').read()); print('syntax OK')"

# Regenerate the UI class after editing the .ui
$PY -m PyQt5.uic.pyuic -x GUI/rapiid_GUI.ui -o GUI/rapiid_GUI.py

# Run the app (needs cameras; see "Verifying" below)
$PY rapiid.py

# Build the frozen app, then the installer (only when asked)
$PY setup.py build
ISCC RAPIID.iss
```
Building inside Dropbox can fail with `[WinError 110]` because Dropbox locks
`rapiid.exe`. If it does, build outside Dropbox and pass
`ISCC /DBuildDir=<path> RAPIID.iss`.

Runtime log: `%LOCALAPPDATA%\RAPIID\logs\rapiid.log`. Ask the user for it when
diagnosing a field problem.

## WHY

- **Users are collection staff, not developers.** They install from the
  installer onto clean machines with no Python or conda. Anything that works
  on the dev machine because conda is on PATH (for example `zlib.dll`, see
  `setup.py`) has to be shipped explicitly.
- **Optional dependencies degrade, never crash.** No FLIR SDK means the FLIR
  options are hidden. No piexif means EXIF is skipped. No ymlRW means the
  config buttons are disabled. Keep every optional import guarded and the app
  running without it.
- **Camera hardware is varied and unforgiving.** Webcams differ in how they
  handle repeated opens, and USB bandwidth problems show up as black frames or
  slow streams rather than errors. Most field bugs are diagnosed from the log,
  so log the facts a remote diagnosis would need.
- **The installer goes into Program Files**, which users can't write to. Logs
  and user data go under `LOCALAPPDATA` or the user's chosen output folder.

## HOW

### Architecture rules
- Camera streaming runs on `QThreadPool` workers. Worker threads update the UI
  only through Qt signals, never by touching widgets directly.
- Always release a camera handle before opening another, and make camera
  selection idempotent. Block signals while restyling combo boxes, because
  restyling re-fires `currentTextChanged`.
- Logging and diagnostics must never be fatal. Wrap them so a failure there
  cannot stop a capture.
- Keep the per-frame path cheap: resize before converting colour, and decode
  every Nth frame with a cached result.
- UI changes go in `GUI/rapiid_GUI.ui`; then regenerate `rapiid_GUI.py`.
- `rapiid.py` is one large file by design. Don't split it into modules unless
  asked.

### Verifying
- There is no test suite. After every edit, run the syntax check at minimum.
- Cameras attached: launch the app and exercise the changed path. None
  attached: use headless scratchpad scripts with mocked cameras or saved frames.

### Versioning and changelog
Each user-facing fix or feature gets a **patch bump** by default (4.3.4 → 4.3.5)
and a CHANGELOG entry. Don't build the exe or installer unless asked.
The version appears in all of these, so update every one:
- `README.md` line 1
- `setup.py` `version=`
- `RAPIID.iss` `AppVersion`, `AppVerName`, `OutputBaseFilename`
- `rapiid.py` EXIF `Software` string
- `GUI/rapiid_GUI.ui` window title, then regenerate `rapiid_GUI.py`
- `CHANGELOG.md` new `## [x.y.z] — YYYY-MM-DD` section

Confirm nothing was missed with `grep -rn "<old version>"`.

CHANGELOG entries go under Added / Changed / Fixed. Each opens with a
**bold sentence describing what the user saw or now sees**, followed by the
cause in plain prose.

### Git
When the version was bumped, append it to the commit subject, e.g.
`Stop leaking webcam handles on camera selection (4.3.3)`.
