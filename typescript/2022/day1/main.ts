import * as fs from "fs";

console.log(
  Math.max(
    ...fs
      .readFileSync("typescript/2022/day1/test.txt", "utf-8")
      .split("\r\n\r\n")
      .map((elf: string) => {
        return elf.split("\r\n").reduce((total, current) => {
          return total + Number(current);
        }, 0);
      })
  )
);

console.log(
  fs
    .readFileSync("typescript/2022/day1/test.txt", "utf-8")
    .split("\r\n\r\n")
    .map((elf: string) => {
      return elf.split("\r\n").reduce((total, current) => {
        return total + Number(current);
      }, 0);
    })
    .sort((a, b) => b - a)
    .slice(0, 3)
    .reduce((total, current) => {
      return total + current;
    })
);