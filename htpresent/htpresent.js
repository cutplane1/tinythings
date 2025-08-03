// array of sections
    // <section>
    //     <h1>First slide!</h1>
    // </section>
    // <section>
    //     <h1>Second slide!</h1>
    // </section>



function st(e,x,y) {
    css = "position: absolute; top: " + x + "px; left: " + y + "px;";
    e.setAttribute("style", css);
}

function features_dispatcher() {
    let coords_f = document.querySelectorAll('[coords]');
    coords_f.forEach((e) => {
        let coords = e.getAttribute('coords').split(' ');
        if (coords.length == 2) {
            let x = parseInt(coords[0]);
            let y = parseInt(coords[1]);
            st(e, x, y);
        } else {
            console.error("invalid coords: ", e);
        }
    });
}

function main() {
    features_dispatcher();
    let sections = document.querySelectorAll('section');
    sections_len = sections.length
    let current_section = 1;

    body = document.querySelector('body');
    body.insertBefore(sections[current_section-1], body.firstChild);


    body.addEventListener("keydown", (event) => {
        if (event.key == 'ArrowRight') {
            current_section++;
            if (current_section > sections_len) {
                current_section = 1;
            }
            body.removeChild(body.firstChild);
            body.insertBefore(sections[current_section-1], body.firstChild);
        }
        if (event.key == 'ArrowLeft') {
            current_section--;
            if (current_section < 1) {
                current_section = sections_len;
            }
            body.removeChild(body.firstChild);
            body.insertBefore(sections[current_section-1], body.firstChild);
        }
    });
}

document.addEventListener("DOMContentLoaded", main);