var gui = require("nw.gui");
let fs = require("fs");

let PACKAGE_SETTINGS = JSON.parse(fs.readFileSync("package.json"));

if (process.platform == "darwin") {
  var menu = new gui.Menu({type: "menubar"});
  menu.createMacBuiltin && menu.createMacBuiltin(window.document.title);
  gui.Window.get().menu = menu;
}

$(function() {
  document.getElementById("close-window-button").onclick = function() {
    window.close();
  };
  $("#title").html(PACKAGE_SETTINGS["title"]);
  $("#version").html("v"+PACKAGE_SETTINGS["version"]);
  $("#license").html(PACKAGE_SETTINGS["license"]);
  $("#description").html(PACKAGE_SETTINGS["description"]);
  $(".author").html(PACKAGE_SETTINGS["author"]["name"])

  gui.Window.get().show();
  setTimeout(function(){
    mainWindow(this)
  }, 2000);

});


function mainWindow(wn){
  nw.Window.open('index.html', {
    position: 'center',
    frame:false,
    show: false,
    min_width: 1000,
    min_height: 600,
    width: 1200,
    height: 600
  },function(new_win) {
      new_win.on('focus', function() {
          wn.close(true);
        });
    });
}
