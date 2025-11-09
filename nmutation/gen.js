function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function last_divisor(n) {
    for (let i = n - 1; i >= 1; i--) {
        if (n % i === 0) {
            return i;
        }
    }
    return 1;
}

function mutate(n) {
    let a = getRandomInt(n) + 1;

    switch (getRandomInt(4)) {
        case 0: return `(${a} + ${n - a})`;
        case 1: return `(${a + n} - ${a})`;
        case 2: {
            if (n > 999) {
                return mutate(n);
            }
            if (a === 0) {
                return `(${n} * 1)`;
            } else {
                return `(${n * a} / ${a})`;
            }
        }
        case 3: {
            if (n > 999) {
                return mutate(n);
            }
            let d = last_divisor(n);
            if (d === n) {
                d = 1;
            }
            return `(${n / d} * ${d})`;
        }
    }
}

function walk(buf, skip_chance = 0.2) {
    return buf.replace(/\d+/g, (match) => {
        if (Math.random() < skip_chance) {
            return match;
        }
        return mutate(parseInt(match));
    });
}
