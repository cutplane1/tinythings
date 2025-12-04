use axum::{
    body::{Body},
    extract::State,
    http::StatusCode,
    response::{IntoResponse, Response},
    routing::get,
    Router,
    extract::Path,
};

use http::header;
use reqwest::Client;

#[tokio::main]
async fn main() {
    let ip = "127.0.0.1:3000";
    let client = Client::new();

    let app = Router::new()
    .route("/", get(|| async { "hi <3" }))
    .route("/{*key}", get(service)).with_state(client);

    let listener = tokio::net::TcpListener::bind(ip).await.unwrap();
    println!("listening on {}", ip);
    axum::serve(listener, app).await.unwrap();
}

pub async fn service(State(client): State<Client>, Path(path): Path<String>) -> Response {
    let mut path = path;

    if !path.starts_with("http") {
        path = format!("https://{}", path);
    }

    let orig_response = match client.get(path).send().await {
        Ok(res) => res,
        Err(err) => {
            return (StatusCode::BAD_REQUEST, Body::new(err.to_string())).into_response();
        }
    };

    let response_builder = Response::builder();

    response_builder
        .status(orig_response.status())
        .header(header::CONTENT_TYPE, "text/html; charset=utf-8")
        .body(Body::from_stream(orig_response.bytes_stream()))
        .unwrap()
}
