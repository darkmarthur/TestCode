const electron = require("electron");
const url = require("url");
const path = require("path");

const { app, BrowserWindow, Menu } = electron;
let mainWindow;
let addWindow;

//Listen for the app to be ready
app.on("ready", () => {
    mainWindow = new BrowserWindow({});
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, "mainWindow.html"),
        protocol: "file:",
        slashes: true
    }));
    mainWindow.on("close", () => app.quit())
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    Menu.setApplicationMenu(mainMenu);
});

function createAddWindow(params) {
    addWindow = new BrowserWindow({
        width: 300,
        height: 200,
        title: "add shopign"
    });
    addWindow.loadURL(url.format({
        pathname: path.join(__dirname, "addWindow.html"),
        protocol: "file:",
        slashes: true
    }));
    addWindow.on("close", () => addWindow = null)

}

const mainMenuTemplate = [
    {},
    label: "File",
    submenu: [
        { label: "add item", click(){
            createAddWindow();
        }},
        { label: "clear items" },
        { label: "quit", 
            accelerator: process.platform == "darwin" ? "Command+Q" : "Ctrl+Q",
            click() {
            app.quit();
        } },
    ]
}]; 