################################################################################
#
# Makefile for LimiFrog-0.x
#
################################################################################

ifeq ($(OS), Windows_NT)
# true for any Windows OS
  UNAME := Windows
else
  UNAME := $(shell uname -s)
endif


# Name of executable
TARGET          = {{target}}

# debugger
DEBUGGER        = DEBUG


# Optimization (0,1,2,s)
OPT             = s

# Directory paths
OBJ_DIR         = ./obj
BIN_DIR         = ./obj


# Linker script
LINKER          = {{LINKER}}

VPATH	:=
{%- for sf in SRC_FOLDER %}
VPATH	:= $(VPATH):{{sf}}
SRC{{loop.index}}_FOLDER = $(notdir $(wildcard {{sf}}))
{%- endfor %}
{%- for af in ASM_FOLDER %}
VPATH	:= $(VPATH):{{af}}
SRC{{loop.index}}_FOLDER = $(notdir $(wildcard {{af}}))
{%- endfor %}

#----------------------------------------------------------------------------
# Creation of list of source files
SOURCES =
{%- for af in ASM_FOLDER %}
SOURCES += $(notdir $(wildcard ./{{af}}/*.s)) 
{%- endfor %}
{%- for sf in SRC_FOLDER %}
SOURCES += $(notdir $(wildcard ./{{sf}}/*.c)) 
{%- endfor %}

INCLUDES =
{%- for f in INCLUDE %}
INCLUDES += {{f}}
{%- endfor %}

ARCH_FLAGS = -mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16

CFLAGS = \
	$(ARCH_FLAGS) \
	$(addprefix -I,$(INCLUDES)) \
	-O$(OPT) \
	-Wall \
	-ffunction-sections \
	-fdata-sections \
	-DSTM32L4 \
	-DSTM32L476xx \
	-DUSE_HAL_DRIVER \
	-D$(DEBUGGER) \
	-fno-exceptions \
	-Wno-write-strings \
	-std=gnu99

LDFLAGS = \
	$(ARCH_FLAGS) \
	-static \
	-Wl,-gc-sections \
	-T$(LINKER)

ASFLAGS = \
	$(ARCH_FLAGS) \
	-x assembler-with-cpp \
	$(addprefix -I,$(INCLUDES))

LIBS =

# Compilation Tools
CC      = arm-none-eabi-gcc
LD      = arm-none-eabi-ld
CP      = arm-none-eabi-objcopy
OD      = arm-none-eabi-objdump
SIZE    = arm-none-eabi-size


TARGET_BIN = $(BIN_DIR)/$(TARGET).bin
TARGET_HEX = $(OBJ_DIR)/$(TARGET).hex
TARGET_LST = $(OBJ_DIR)/$(TARGET).lst
TARGET_ELF = $(OBJ_DIR)/$(TARGET).elf
TARGET_OBJ = $(addsuffix .o,$(addprefix $(OBJ_DIR)/,$(basename $(SOURCES))))

#-------------------------------------------------------------------------------#

ifneq ($(UNAME), Windows)
 all:  build size
endif

ifeq ($(UNAME), Windows)
  all: $(TARGET_BIN) $(TARGET_HEX) $(TARGET_LST)
else
  build: $(TARGET_BIN) $(TARGET_HEX) $(TARGET_LST)
endif

$(TARGET_BIN): $(TARGET_ELF)
	@echo "-> "$(notdir $@)""
	@$(CP) -O binary $< $@

$(TARGET_HEX): $(TARGET_ELF)
	@echo "-> "$(notdir $@)""
	@$(CP) -O ihex $< $@

$(TARGET_LST): $(TARGET_ELF)
	@echo "-> "$(notdir $@)""
	@$(OD) -S $< > $@

$(TARGET_ELF): $(TARGET_OBJ)
	@echo -e "\033[01;33m==========  GENERATION  ====================================\033[m"
	@echo "-> "$(notdir $@)""
	@$(CC)  $(LDFLAGS) -o  $@  $^ $(LIBS)

$(OBJ_DIR)/%.o: %.c
ifeq ($(UNAME), Windows)
#	@mkdir $(dir $@)  /* Option -p inexistent in Windows, covered by default */
else
	@mkdir -p $(dir $@)
endif
	@echo -e "\033[01;42m-> COMPILE:\033[m "$(notdir $<)
	@$(CC) $(CFLAGS) -c -o $@ $<

$(OBJ_DIR)/%.o: %.cpp
ifeq ($(UNAME), Windows)
#	@mkdir $(dir $@)  /* Option -p inexistent in Windows, covered by default */
else
	@mkdir -p $(dir $@)
endif
	@echo -e "\033[01;42m-> COMPILE:\033[m "$(notdir $<)
	@$(CC) $(CFLAGS) -c -o $@ $<

$(OBJ_DIR)/%.o: %.s
ifeq ($(UNAME), Windows)
#	@mkdir $(dir $@)  /* Option -p inexistent in Windows, covered by default */
else
	@mkdir -p $(dir $@)
endif
	@echo -e "\033[01;42m-> COMPILE:\033[m "$(notdir $<)
	@$(CC) $(ASFLAGS) -c -o $@ $<

run: $(TARGET_BIN)
	@echo -e "\033[01;33m==========  PROGRAMMING  =================================\033[m"
	@st-flash write $< 0x8000000

size: $(TARGET_ELF)
	@echo -e "\033[01;33m==========  SIZE  ========================================\033[m"
	@$(SIZE) $<

clean:
	@echo -e "\033[01;41m-> SUPRESSION !\033[m"
	@rm -vf $(TARGET_BIN)
	@rm -vf $(TARGET_HEX)
	@rm -vf $(TARGET_LST)
	@rm -vf $(TARGET_ELF)
ifeq ($(UNAME), Windows)
	@rm -vf $(OBJ_DIR)/*.o
else
	@rm -vf $(SRC_DIR)/*~
endif

purge:
	@echo -e "\033[01;41m-> SUPRESSION !!\033[m"
	@rm -vRf $(OBJ_DIR)



help:
	@echo ""
	@echo "#==============================================================#"
	@echo "#                                                              #"
	@echo "# Usage: make [options]                                        #"
	@echo "#                                                              #"
	@echo "#  options:                                                    #"
	@echo "#   build     compile complete project (with *.o)              #"
	@echo "#   run       program STM32 on the board                       #"
	@echo "#   size      show size of binary                              #"
	@echo "#   clean     erase files *.bin *.hex *.lst *.elf *~           #"
	@echo "#   purge     erase directory:   obj/                          #"
	@echo "#   help      show this help                                   #"
	@echo "#==============================================================#"
	@echo ""

#----------------------------------------------------------------------------------
