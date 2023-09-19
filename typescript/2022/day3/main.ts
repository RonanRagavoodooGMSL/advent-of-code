import * as fs from "fs";

const words: string[] = fs
  .readFileSync("typescript/2022/day3/test.txt", "utf-8")
  .split("\r\n");

const values: { [key: string]: number } = {};
const low: string[] = Array.from(Array(26))
  .map((e, i) => i + 97)
  .map((x) => String.fromCharCode(x));
const upp: string[] = Array.from(Array(26))
  .map((e, i) => i + 65)
  .map((x) => String.fromCharCode(x));
low.forEach((letter) => (values[letter] = low.indexOf(letter) + 1));
upp.forEach((letter) => (values[letter] = upp.indexOf(letter) + 27));

const set: Set<string> = new Set();
words
  .map((items) => [
    items.slice(0, items.length / 2),
    items.slice(items.length / 2, items.length),
  ])
  .map((item) =>
    item[0].split("").map((letter) => {
      if (item[1].includes(letter)) {
        set.add(letter);
      }
    })
  );

const res = [...set].reduce((total: number, current: string) => {
  return total + values[current];
}, 0);

console.log(res);
