#!/usr/bin/node
exports.esrever = function (list) {
    let len = list.length;
    for (let i = 0; i < (len / 2); i++) {
        // swap
        [list[i], list[len - i - 1]] = [list[len - i - 1], list[i]];
    }
    return list;
}
