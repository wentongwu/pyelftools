#-------------------------------------------------------------------------------
# elftools: elf/enums.py
#
# Mappings of enum names to values
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------------

# e_ident[EI_CLASS] in the ELF header
ENUM_EI_CLASS = dict(
    ELFCLASSNONE=0,
    ELFCLASS32=1,
    ELFCLASS64=2
)

# e_ident[EI_DATA] in the ELF header
ENUM_EI_DATA = dict(
    ELFDATANONE=0,
    ELFDATA2LSB=1,
    ELFDATA2MSB=2
)

# e_version in the ELF header
ENUM_E_VERSION = dict(
    EV_NONE=0,
    EV_CURRENT=1
)

# e_ident[EI_OSABI] in the ELF header
ENUM_EI_OSABI = dict(
    ELFOSABI_SYSV=0,
    ELFOSABI_HPUX=1,
    ELFOSABI_NETBSD=2,
    ELFOSABI_LINUX=3,
    ELFOSABI_HURD=4,
    ELFOSABI_SOLARIS=6,
    ELFOSABI_AIX=7,
    ELFOSABI_IRIX=8,
    ELFOSABI_FREEBSD=9,
    ELFOSABI_TRU64=10,
    ELFOSABI_MODESTO=11,
    ELFOSABI_OPENBSD=12,
    ELFOSABI_OPENVMS=13,
    ELFOSABI_NSK=14,
    ELFOSABI_AROS=15,
    ELFOSABI_ARM=97,
    ELFOSABI_STANDALONE=255,
)

# e_type in the ELF header
ENUM_E_TYPE = dict(
    ET_NONE=0,
    ET_REL=1,
    ET_EXEC=2,
    ET_DYN=3,
    ET_CORE=4,
    ET_LOPROC=0xff00,
    ET_HIPROC=0xffff,
    _default_='PROC_SPECIFIC',
)

# e_machine in the ELF header
# (this list is currently somewhat partial...)
ENUM_E_MACHINE = dict(
    EM_NONE=0,
    EM_M32=1,
    EM_SPARC=2,
    EM_386=3,
    EM_68K=4,
    EM_88K=5,
    EM_860=7,
    EM_MIPS=8,
    EM_S370=9,
    EM_MIPS_RS4_BE=10,
    EM_IA_64=50,
    EM_X86_64=62,
    EM_AVR=83,
    _default_='RESERVED',
)

# sh_type in the section header
ENUM_SH_TYPE = dict(
    SHT_NULL=0,
    SHT_PROGBITS=1,
    SHT_SYMTAB=2,
    SHT_STRTAB=3,
    SHT_RELA=4,
    SHT_HASH=5,
    SHT_DYNAMIC=6,
    SHT_NOTE=7,
    SHT_NOBITS=8,
    SHT_REL=9,
    SHT_SHLIB=10,
    SHT_DYNSYM=11,
    SHT_INIT_ARRAY=14,
    SHT_FINI_ARRAY=15,
    SHT_PREINIT_ARRAY=16,
    SHT_GROUP=17,
    SHT_SYMTAB_SHNDX=18,
    SHT_NUM=19,
    SHT_LOOS=0x60000000,
    SHT_HIOS=0x6fffffff,
    SHT_LOPROC=0x70000000,
    SHT_HIPROC=0x7fffffff,
    SHT_LOUSER=0x80000000,
    SHT_HIUSER=0xffffffff,
    SHT_AMD64_UNWIND=0x70000001,
    _default_='RESERVED',
)

# p_type in the program header
# some values scavenged from the ELF headers in binutils-2.21
ENUM_P_TYPE = dict(
    PT_NULL=0,
    PT_LOAD=1,
    PT_DYNAMIC=2,
    PT_INTERP=3,
    PT_NOTE=4,
    PT_SHLIB=5,
    PT_PHDR=6,
    PT_LOPROC=0x70000000,
    PT_HIPROC=0x7fffffff,
    PT_GNU_EH_FRAME=0x6474e550,
    PT_GNU_STACK=0x6474e551,
    PT_GNU_RELRO=0x6474e552,
)

# st_info bindings in the symbol header
ENUM_ST_INFO_BIND = dict(
    STB_LOCAL=0,
    STB_GLOBAL=1,
    STB_WEAK=2,
    STB_NUM=3,
    STB_LOOS=10,
    STB_HIOS=12,
    STB_LOPROC=13,
    STB_HIPROC=15,
)

# st_info type in the symbol header
ENUM_ST_INFO_TYPE = dict(
    STT_NOTYPE=0,
    STT_OBJECT=1,
    STT_FUNC=2,
    STT_SECTION=3,
    STT_FILE=4,
    STT_COMMON=5,
    STT_TLS=6,
    STT_NUM=7,
    STT_LOOS=10,
    STT_HIOS=12,
    STT_LOPROC=13,
    STT_HIPROC=15,
)
