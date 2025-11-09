function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function mutate(n) {
    let a = getRandomInt(n) + 1;

    switch (getRandomInt(2)) {
        case 0: return `(${a} + ${n - a})`;
        case 1: return `(${a+n} - ${a})`;
    }
}

function walk(buf, skip_chance = 0.3) {

    return buf.replace(/\d+/g, (match) => {
        if (Math.random() > skip_chance) {
            return match;
        }
        return mutate(parseInt(match));
    });
}
