import * as fs from "fs";

const tree = {};
const curr_dir: string[] = [];
const sizes: number[] = [];
let res: number = 0;

const recurse = (path: string) => {
  const lst = tree[path];
  let total = 0;
  lst.forEach((element) => {
    if (isNaN(element)) {
      total += recurse(`${path}/${element}`);
    } else {
      total += Number(element);
    }
  });
  res += total < 100000 ? total : 0;
  return total;
};

const recurse2 = (path: string) => {
  const lst = tree[path];
  let total = 0;
  lst.forEach((element) => {
    if (isNaN(element)) {
      total += recurse2(`${path}/${element}`);
    } else {
      total += Number(element);
    }
  });
  sizes.push(total);
  return total;
};

const data = fs
  .readFileSync("typescript/2022/day7/test.txt", "utf-8")
  .split("\r\n")
  .filter((line) => !line.startsWith("$ ls"))
  .forEach((element) => {
    const pair: string[] = element.split(" ");
    if (element.startsWith("$ cd")) {
      pair[2] === ".." ? curr_dir.pop() : curr_dir.push(pair[2]);
    } else {
      if (curr_dir.join("/") in tree) {
        tree[curr_dir.join("/")].push(pair[0] === "dir" ? pair[1] : pair[0]);
      } else {
        tree[curr_dir.join("/")] = [pair[0] == "dir" ? pair[1] : pair[0]];
      }
    }
  });
recurse("/");
console.log(res);

const free_space = recurse2("/") - 40000000;
console.log(Math.min(...sizes.filter((x) => x > free_space)));
