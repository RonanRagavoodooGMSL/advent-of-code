import * as fs from "fs";

const rucksacks: string[] = fs
  .readFileSync("typescript/2022/day3/test.txt", "utf-8")
  .split("\r\n");

const values: { [key: string]: number } = {};
const low: string[] = Array.from(Array(26))
  .map((_, i) => i + 97)
  .map((x) => String.fromCharCode(x));
const upp: string[] = Array.from(Array(26))
  .map((_, i) => i + 65)
  .map((x) => String.fromCharCode(x));
low
  .concat(upp)
  .forEach((letter) => (values[letter] = low.concat(upp).indexOf(letter) + 1));

// Part 1

const part1Array: number[] = [];

rucksacks
  .map((items) => [
    items.slice(0, items.length / 2),
    items.slice(items.length / 2, items.length),
  ])
  .map((item) => {
    const set: Set<number> = new Set();
    item[0].split("").map((letter) => {
      if (item[1].includes(letter)) {
        set.add(values[letter]);
      }
    });
    part1Array.push(...set);
  });

const part1: number = part1Array.reduce((total: number, curr: number) => {
  return total + curr;
}, 0);

console.log(part1);

// Part 2

const groups: string[][] = [];
for (let i = 0; i < rucksacks.length; i += 3) {
  groups.push(rucksacks.slice(i, i + 3));
}

const part2Array: number[] = [];
groups.map((group) => {
  const set: Set<number> = new Set();
  [...group[0]].forEach((letter) => {
    group[1].includes(letter) &&
      group[2].includes(letter) &&
      set.add(values[letter]);
  });
  part2Array.push(...set);
});

const part2: number = part2Array.reduce((total, curr) => total + curr);

console.log(part2);
