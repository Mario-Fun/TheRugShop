const users = [{name: "Mario", handle: "0xmari0"}, {name: "Alex", handle: "alexkfine"}, {name: "Omar", handle: "omarameme"}, {name: "Amila", handle: "VitalikButerin"}];

var currUserIdx = 0;

function onLoad() {
    const body = document.getElementById("body");

    body.appendChild(createTitle());
    body.appendChild(createMainView());
    body.appendChild(createToggleButtons());
}

function createTitle() {
    const title = document.createElement("div");
    title.style.display = "flex";
    title.style.justifyContent = "center";
    title.style.alignItems = "center";
    title.style.margin = "20px";

    title.appendChild(createTitleLabel());

    return title;
}

function createTitleLabel() {
    const label = document.createElement("div");
    label.style.fontFamily = "DrukWideMedium";
    label.style.fontSize = "40px";
    label.innerHTML = "Welcome to the Laundromat";
    return label;
}

function createMainView() {
    const mainView = document.createElement("div");
    mainView.id = "mainView";

    mainView.style.display = "flex";
    mainView.style.justifyContent = "center";
    mainView.style.alignItems = "center";

    mainView.style.height = "500px";
    mainView.style.margin = "auto";
    mainView.style.width = "800px";
    mainView.style.marginTop = "100px";
    mainView.style.fontFamily = "Inter Regular";

    mainView.appendChild(createWashtraderPic());
    mainView.appendChild(createWashtraderInfo());

    return mainView;
}

function createWashtraderInfo() {
    const washtraderInfo = document.createElement("div");

    washtraderInfo.appendChild(createWashtraderIntro());
    washtraderInfo.appendChild(createWashtradedProject());
    washtraderInfo.appendChild(createWashtradedNumber());

    return washtraderInfo;
}

function createWashtraderPic() {
    const washtraderPic = document.createElement("img");

    washtraderPic.src = "https://twitter-profile-pic.jsoxford.com/" + users[currUserIdx].handle + "?size=original";
    washtraderPic.style.width = "200px";
    washtraderPic.style.height = "200px";
    washtraderPic.style.margin = "40px";

    return washtraderPic;
}

function createWashtraderIntro() {
    const intro = document.createElement("div");
    intro.style.fontSize = "30px";
    intro.style.marginBottom = "50px";
    intro.innerHTML = "Hi, my name is " + users[currUserIdx].name + " and I'm a washtrader!";
    return intro;
}

function createWashtradedProject() {
    const project = document.createElement("div");
    project.innerHTML = "Project washtraded: AcclimatedMoonCats (0xc3f733ca98E0daD0386979Eb96fb1722A1A05E69)";
    project.style.marginBottom = "20px";
    return project;
}

function createWashtradedNumber() {
    const number = document.createElement("div");
    number.innerHTML = "Number of wash cycles: 7";
    return number;
}

function createToggleButtons() {
    const toggleButtons = document.createElement("div");
    toggleButtons.id = "toggleButtons";
    toggleButtons.style.display = "flex";
    toggleButtons.style.justifyContent = "center";
    toggleButtons.style.alignItems = "center";
    toggleButtons.style.columnGap = "40px";
    toggleButtons.style.marginTop = "200px";

    toggleButtons.appendChild(createLeftToggleButton());
    toggleButtons.appendChild(createRightToggleButton());

    return toggleButtons;
}

function createLeftToggleButton() {
    const leftToggleButton = document.createElement("img");
    leftToggleButton.src = "leftArrow.png";
    leftToggleButton.style.width = "100px";

    leftToggleButton.onmouseover = () => {
        document.body.style.cursor = "pointer";
    };

    leftToggleButton.onmouseleave = () => {
        document.body.style.cursor = "default";
    };

    leftToggleButton.onclick = () => {
        if (currUserIdx == 0) {
            currUserIdx = users.length - 1;
        } else {
            currUserIdx -= 1;
        }
        recreateMainView();
    };

    return leftToggleButton;
}

function createRightToggleButton() {
    const rightToggleButton = document.createElement("img");
    rightToggleButton.src = "rightArrow.png";
    rightToggleButton.style.width = "100px";

    rightToggleButton.onmouseover = () => {
        document.body.style.cursor = "pointer";
    };

    rightToggleButton.onmouseleave = () => {
        document.body.style.cursor = "default";
    };

    rightToggleButton.onclick = () => {
        if (currUserIdx + 1 == users.length) {
            currUserIdx = 0;
        } else {
            currUserIdx += 1;
        }
        recreateMainView();
    };

    return rightToggleButton;
}

function recreateMainView() {
    const mainView = document.getElementById("mainView");
    mainView.remove();
    const toggleButtons = document.getElementById("toggleButtons");
    toggleButtons.remove();
    body.appendChild(createMainView());
    body.appendChild(createToggleButtons());
}