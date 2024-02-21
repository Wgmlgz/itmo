/* eslint-disable @typescript-eslint/no-var-requires */
const { app, BrowserWindow } = require('electron');
const serve = require('electron-serve');
const ws = require('electron-window-state');

const path = require('path');

try {
  require('electron-reload')(__dirname, {
    electron: path.join(__dirname, '..', 'node_modules', '.bin', 'electron')
  });
} catch {
  /* empty */
}

const loadURL = serve({ directory: '.' });

/**
 * @type {number}
 */
const port = Number(process.env.PORT || 4173);
const is_dev = !app.isPackaged || process.env.NODE_ENV == 'development';

/**
 * @type {BrowserWindow | null}
 */
let main_window = null;

/**
 * @param {number} port
 */
function loadVite(port) {
  main_window?.loadURL(`http://localhost:${port}`).catch(() => {
    setTimeout(() => {
      loadVite(port);
    }, 200);
  });
}

function createMainWindow() {
  let mws = ws({
    defaultWidth: 1000,
    defaultHeight: 800
  });

  main_window = new BrowserWindow({
    x: mws.x,
    y: mws.y,
    width: mws.width,
    height: mws.height,
    fullscreen: true,
    
    
    webPreferences: {
      sandbox: false,
      nodeIntegration: true,
      contextIsolation: false,
      devTools: is_dev || true
    }
  });

  main_window.once('close', () => {
    main_window = null;
  });

  if (!is_dev) main_window.removeMenu();
  else main_window.webContents.openDevTools();
  mws.manage(main_window);

  if (is_dev) loadVite(port);
  else loadURL(main_window);
}
app.commandLine.appendSwitch('enable-features', 'SharedArrayBuffer');
app.commandLine.appendSwitch('no-sandbox');
app.commandLine.appendSwitch('--no-sandbox');
app.commandLine.appendArgument('--no-sandbox');
app.commandLine.appendArgument('no-sandbox');

app.once('ready', createMainWindow);
app.on('activate', () => {
  if (!main_window) createMainWindow();
});
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
