const foo = Bun.file("multiply_by_two.tsk");

console.log(await foo.text());