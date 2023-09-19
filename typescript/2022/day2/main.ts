import * as fs from "fs";

const words: string[] = fs
  .readFileSync("typescript/2022/day2/test.txt", "utf-8")
  .split("\r\n");

const wins: { [key: string]: string } = {
  ROCK: "SCISSORS",
  PAPER: "ROCK",
  SCISSORS: "PAPER",
};
const symbols: { [key: string]: string } = {
  A: "ROCK",
  B: "PAPER",
  C: "SCISSORS",
  X: "ROCK",
  Y: "PAPER",
  Z: "SCISSORS",
};
const symbol_score: { [key: string]: number } = {
  ROCK: 1,
  PAPER: 2,
  SCISSORS: 3,
};

const sum = words.reduce((total: number, current: string) => {
  const pairs = current.split(" ");
  return (total +=
    wins[symbols[pairs[1]]] === symbols[pairs[0]]
      ? symbol_score[symbols[pairs[1]]] + 6
      : symbols[pairs[0]] === symbols[pairs[1]]
      ? symbol_score[symbols[pairs[1]]] + 3
      : symbol_score[symbols[pairs[1]]]);
}, 0);

sum;
