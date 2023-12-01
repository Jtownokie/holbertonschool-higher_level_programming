#!/usr/bin/node
const testArray = ["example.com/1", "example.com/4", "example.com/3", "example.com/4"]

for (const item of testArray) {
  if (item.includes("/1")) {
    console.log("Found");
  }
}
