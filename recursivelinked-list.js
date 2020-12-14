class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}


class LinkedList {
    constructor() {
        this.head = null;
    }
    append(val) {
        if (this.head === null) {
            this.head = new Node(val);
            return;
        }
        this._append(val, this.head)
    }

    _append(val, curr) {
        if (curr.next === null) {
            curr.next = new Node(val);
            return;
        }
        this._append(val, curr.next);
    }

    print() {
        const output = this._print(this.head);
        console.log(output);

    }
    _print(curr) {
        if (curr === null) return '';
        return curr.val + '->' + this._print(curr.next);
    }
    constains(target) {
        return this._constains(this.head);
    }

    _constains(target, curr) {
        if (curr === null) return false;
        if (curr.val === target) return true;
        return this._constains(target, curr.next);

    }


}

const list = new LinkedList();
list.append('a');
list.append('b');
list.append('c');
list.append('d');

list.print();

console.log(list.append('a'));
console.log(list.append('b'));
console.log(list.append('c'));
console.log(list.append('d'));