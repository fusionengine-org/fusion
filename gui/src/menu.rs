use gtk::*;
use gtk::prelude::*;

pub fn ui(app: &Application) {
    // Create a window and set the title
    let window = ApplicationWindow::builder()
        .application(app)
        .title("My GTK App")
        .build();

    window.present();
}