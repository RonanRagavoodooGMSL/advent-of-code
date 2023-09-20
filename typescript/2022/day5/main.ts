import * as fs from "fs";

const data = fs
  .readFileSync("typescript/2022/day5/test.txt", "utf-8")
  .split("\r\n\r\n");

const res = data[0]
  .split("\r\n")
  .slice(0, data[0].split("\r\n").length - 1)
  .map((item: string) => {
    return item.match(/.{1,4}/g);
  });

const zip = res[0]
  .map((_: string, index: number) => res.map((row: string[]) => row[index]))
  .map((col: string[]) =>
    col
      .map((item) => {
        return item.trim().length !== 0 && _.trim(item, "[] ");
      })
      .filter((i: any) => i !== false)
  );

data[1]
  .split("\r\n")
  .map((move: string) =>
    move
      .split("")
      .map((char: string) => {
        return !isNaN(parseInt(char, 10)) && Number(char);
      })
      .filter((i: any) => i !== false)
  )
  .map((move: number[]) => {
    zip[move[2] - 1] = [
      ...zip[move[1] - 1].slice(0, move[0]).reverse(),
      ...zip[move[2] - 1],
    ];
    zip[move[1] - 1] = zip[move[1] - 1].slice(move[0], zip[move[1] - 1].length);
  });

const ans = zip.map((col: string[]) => col[0]).join("");
ans;
