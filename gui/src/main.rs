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
    app.connect_activate(menu::ui);

    // Run the application
    app.run()
}