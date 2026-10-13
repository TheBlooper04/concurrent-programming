CC		:= gcc
CFLAGS	:= -O0 -Wall -Wextra

OBJS_DIR	:= obj/
EXECS_DIR	:= bin/

SRCS	:= $(wildcard *.c)
OBJS	:= $(patsubst %.c,$(OBJS_DIR)%.o,$(SRCS))
EXECS	:= $(patsubst %.c,$(EXECS_DIR)%,$(SRCS))

all: $(EXECS)

$(EXECS_DIR)%: $(OBJS_DIR)%.o
	$(CC) $(CFLAGS) $< -o $@ 

$(OBJS_DIR)%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

cdirs:
	mkdir $(OBJS_DIR) $(EXECS_DIR)

clean:
	rm -r $(OBJS_DIR) $(EXECS_DIR)

.PHONY: all cdirs clean