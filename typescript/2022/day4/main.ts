import * as fs from "fs";

const part1: number = fs
  .readFileSync("typescript/2022/day4/test.txt", "utf-8")
  .split("\r\n")
  .map((item: string) => item.split(","))
  .reduce((total: number, pair: string[]) => {
    const pair1 = pair[0].split("-");
    const pair2 = pair[1].split("-");
    const first = _.range(Number(pair1[0]), Number(pair1[1]) + 1);
    const second = _.range(Number(pair2[0]), Number(pair2[1]) + 1);
    if (
      first.every((x: number) => second.includes(x)) ||
      second.every((y: number) => first.includes(y))
    ) {
      return total + 1;
    }
    return total;
  }, 0);

const part2: number = fs
  .readFileSync("typescript/2022/day4/test.txt", "utf-8")
  .split("\r\n")
  .map((item: string) => item.split(","))
  .reduce((total: number, pair: string[]) => {
    const pair1 = pair[0].split("-");
    const pair2 = pair[1].split("-");
    const first = _.range(Number(pair1[0]), Number(pair1[1]) + 1);
    const second = _.range(Number(pair2[0]), Number(pair2[1]) + 1);
    if (first.filter((x: string) => second.includes(x)).length !== 0) {
      return total + 1;
    }
    return total;
  }, 0);

part1;
part2;
