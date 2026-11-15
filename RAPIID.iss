; Where the cx_Freeze output lives. Defaults to the in-tree build directory,
; but can be pointed elsewhere with:  ISCC /DBuildDir=<path> RAPIID.iss
; Building outside a Dropbox-synced folder avoids cx_Freeze failing with
; "[WinError 110] The system cannot open the device or file specified" when
; Dropbox locks rapiid.exe between stamping it and writing its resources.
#ifndef BuildDir
  #define BuildDir "build\exe.win-amd64-3.8"
#endif

[Setup]
AppId={{8AAE16EC-C49C-439A-9B9C-1541DC8A1807}
AppName=RAPIID
AppVersion=4.3.4
AppVerName=RAPIID 4.3.4
AppPublisher=Aaron Harmer
AppPublisherURL=https://github.com/aharmer/RAPIID
DefaultDirName={autopf64}\RAPIID
DefaultGroupName=RAPIID
UninstallDisplayIcon={app}\rapiid.exe
OutputDir=dist
OutputBaseFilename=RAPIID-4.3.4-win64-setup
SetupIconFile=images\RAPIID_icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64compatible
CloseApplications=yes
PrivilegesRequiredOverridesAllowed=dialog

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"

[Files]
Source: "{#BuildDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\RAPIID"; Filename: "{app}\rapiid.exe"; IconFilename: "{app}\images\RAPIID_icon.ico"
Name: "{autodesktop}\RAPIID"; Filename: "{app}\rapiid.exe"; IconFilename: "{app}\images\RAPIID_icon.ico"; Tasks: desktopicon

[Run]
Filename: "{app}\rapiid.exe"; Description: "Launch RAPIID"; Flags: nowait postinstall skipifsilent
