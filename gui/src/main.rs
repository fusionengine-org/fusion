use gtk::prelude::*;
use gtk::*;
mod menu;

const APP_ID: &str = "org.fusion-engine.gui";

fn main() -> glib::ExitCode {
    let app = Application::builder().application_id(APP_ID).build();

    app.connect_activate(window);

    app.run()
}

pub fn window(app: &Application) {
    let window = ApplicationWindow::builder()
        .application(app)
        .title("Fusion Engine")
        .default_width(800)
        .default_height(600)
        .build();

    menu::menu(&window);

    window.present();
}
