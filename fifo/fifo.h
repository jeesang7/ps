#ifndef __FIFO_H__
#define __FIFO_H__

#include <stddef.h>
#include <stdbool.h>

struct fifo {
    size_t n;       // number of items
    unsigned int front, rear;
    void *buf;
};

void fifo_init(struct fifo *q, void *queue, size_t n);
void fifo_flush(struct fifo *q);
bool fifo_empty(struct fifo *q);

int fifo_pushb(struct fifo *q, int val);
int fifo_popb(struct fifo *q);

void fifo_test(void);

#endif