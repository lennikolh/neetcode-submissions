class DynamicArray {
    private:
    int capacity;
    int length;
    int* arr;
public:

    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->length = 0;
        this->arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if(length==capacity) {
            resize();
        }
        arr[length] = n;
        length++;
    }

    int popback() {
        length--;
        return arr[length];
    }

    void resize() {
        capacity *= 2;
        int* newArr = new int[capacity];
        for (int i = 0; i<length; i++)
        newArr[i] = arr[i];
        delete[] arr;
        arr = newArr;

    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return capacity;
    }
};
