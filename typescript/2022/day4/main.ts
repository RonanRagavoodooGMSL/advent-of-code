import * as fs from "fs";
import range from "lodash";

const res: number = fs
  .readFileSync("typescript/2022/day4/test.txt", "utf-8")
  .split("\r\n")
  .map((item: string) => item.split(","))
  .reduce((total: number, pair: string[]) => {
    const first = _.range(
      Number(pair[0].charAt(0)),
      Number(pair[0].charAt(2)) + 1
    ).join(",");
    const second = _.range(
      Number(pair[1].charAt(0)),
      Number(pair[1].charAt(2)) + 1
    ).join(",");
    if (first.includes(second) || second.includes(first)) {
      return total + 1;
    } else {
      return total;
    }
  }, 0);

res;
