class Directory {
	constructor(directory_id, icon) {
		this.icon = icon;

		this.directory_id = directory_id;
		if (!icon) {
			this.directory = document.getElementById(this.directory_id);
		} else {
			this.directory = document.getElementById("Homepage");
		}

		this.navbar = document.getElementById("navbar");
		if (!icon) {
			this.navbar_directory_id = this.directory_id + "_directory";
		} else {
			this.navbar_directory_id = "Homepage_directory"
		}

		this.add_to_navbar();

		var _this = this;

		if (!icon) {
			this.navbar_directory.addEventListener("click", function () { _this.show(); });
		} else {
			document.getElementById(this.directory_id).addEventListener("click", function () { _this.show() });
		}
	}

	add_to_navbar() {
		if (!this.icon) {
			var element = document.createElement("h6");
			var text_node = document.createTextNode(this.directory_id.split("_").join(" "));
			element.appendChild(text_node);

			element.classList = "navbar_directory";
			element.id = this.directory_id + "_directory";

			this.navbar.appendChild(element);

			this.navbar_directory = document.getElementById(this.navbar_directory_id);
		} else {
			this.navbar_directory = document.getElementById("Homepage_directory");
		}
	}

	show() {
		var _this = this;

		for (var i in directory_list) {
			directory_list[i].hide();
		}

		this.navbar_directory.classList.add("navbar_directory_focus");

		window.scroll({ top: 0, left: 0, behavior: "smooth" });

		setTimeout(function () { _this.directory.style.removeProperty("display"); }, 500);
		setTimeout(function () { _this.directory.classList.add("focus"); }, 520);

		if (!this.icon) {
			document.title = "Noxellar | " + this.directory_id.split("_").join(" ");
		} else {
			document.title = "Noxellar | Homepage";
		}
	}

	hide() {
		var _this = this;

		this.navbar_directory.classList.remove("navbar_directory_focus");

		this.directory.classList.remove("focus");
		setTimeout(function () { _this.directory.style.display = "none"; }, 500);
	}
}

var directory_list = {};

var directories = document.getElementsByClassName("directory");

for (var i = 0; i < directories.length; i++) {
	var directory_id = directories[i].id;
	directory_list[directory_id] = new Directory(directory_id, false);
}

var Icon = new Directory("icon", true)

directory_list.Homepage.show();