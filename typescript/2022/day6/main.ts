import * as fs from "fs";

const data = fs
  .readFileSync("typescript/2022/day6/test.txt", "utf-8")
  .split("");

for (let i = 0; i < data.length; i++) {
  const set: Set<string> = new Set(data.slice(i, i + 4));
  if (set.size === 4) {
    console.log(i + 4);
    break;
  }
}
