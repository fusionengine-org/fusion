use gtk::prelude::*;
use gtk::*;
mod menu;

const APP_ID: &str = "org.fusion-engine.gui";

fn main() -> glib::ExitCode {
    // Create a new application
    let app = Application::builder()
        .application_id(APP_ID)
        .build();

    // Connect to "activate" signal of `app`
    app.connect_activate(window);

    // Run the application
    app.run()
}

pub fn window(app: &Application) {
    // Create a window and set the title
    let window = ApplicationWindow::builder()
        .application(app)
        .title("My GTK App")
        .default_width(800)
        .default_height(600)
        .build();

    menu::menu(&window);    

    window.present();
}