#include "fifo.h"
#include "atomic.h"         // Note: __LDREXW and __STREXW are CMSIS function

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <errno.h>


void fifo_init(struct fifo *q, void *queue, size_t n) {
    q->n = n;
    q->buf = queue;
    q->front = q->rear = 0;
}

void fifo_flsh(struct fifo *q) {
    q->front = q->rear = 0;
}

bool fifo_isempty(struct fifo *q) {
    return q->front == q->rear;
}

int fifo_pushb(struct fifo *q, int val) {
    unsigned int pos;
    char *buf;

    if ( !q || !q->buf )
        return -EINVAL;

    buf = q->buf;

    do {
        pos = __LDREWX((volatile uint32_t *)&q->rear);

        if ( ((pos+1) % q->n) == *(volatile typeof(q->front) *)&q->front )
            return -ENOSPC;         // no more room

        buf[pos] = (typeof(*buf))val;
        pos = (pos+1) % q->n;
    } while(__STREXW(pos, (volatile uint32_t *)&q->rear));

    return 0;
}

int fifo_popb(struct fifo *q) {
    unsigned int pos;
    char *buf;
    int val;

    if ( !q || !q->buf )
        return -EINVAL;

    buf = q->buf;

    do {
        pos = __LDREWX((volatile uint32_t *)&q->front);

        if ( pos == *(volatile typeof(q->rear) *)&q->rear )
            return -ENOENT;     // empty
        
        val = (typeof(val))buf[pos];
        pos = (pos+1) % q->n;
    } while(__STREXW(pos, (volatile uint32_t*)&q->front));

    return val;
}

void fifo_test(void) {
    printf("fifo test...\n");

    struct fifo *f;
    int q_set[20] = {1, 2, 3, 4, 5};
    char* val;
    
    fifo_init(f, q_set, 20);

    // printf("pop %d \n", 2);
    // printf("pop %d \n", fifo_popb(f));
    // printf("pop %d \n", fifo_popb(f));

    // fifo_pushb(f, 6);
    // fifo_pushb(f, 7);
    // fifo_pushb(f, 8);

    // printf("pop %d\n", fifo_popb(f));
    // printf("pop %d\n", fifo_popb(f));
    // printf("pop %d\n", fifo_popb(f));

}