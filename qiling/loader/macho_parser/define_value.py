# magic
MAGIC_X86               = 0xFEEDFACE
MAGIC_X8664             = 0xFEEDFACF
MAGIC_FAT               = 0xBEBAFECA

# cpu type
CPU_TYPE_X8664          = 0x01000007
CPU_TYPE_X86            = 0x00000007
CPU_SUBTYPE_X8664_ALL   = 0x00000030
CPU_SUBTYPE_i386_ALL    = 0x00000030

# file type
MH_DYLINKER             = 0x00000007
MH_EXECUTE              = 0x00000002

# load command 
LC_SEGMENT_64           = 0x00000019
LC_SEGMENT              = 0x00000001
LC_SYMTAB               = 0x00000002
LC_DYSYMTAB             = 0x0000000B
LC_ID_DYLINKER          = 0x0000000F
LC_UUID                 = 0x0000001B
LC_VERSION_MIN_MACOSX   = 0x00000024
LC_SOURCE_VERSION       = 0x0000002A
LC_UNIXTHREAD           = 0x00000005
LC_SEGMENT_SPLIT_INFO   = 0x0000001E
LC_FUNCTION_STARTS      = 0x00000026
LC_DATA_IN_CODE         = 0x00000029
LC_CODE_SIGNATURE       = 0x0000001D
LC_DYLD_INFO_ONLY       = 0x80000022
LC_LOAD_DYLINKER        = 0x0000000E
LC_MAIN                 = 0x80000028
LC_LOAD_DYLIB           = 0x0000000C

# UNIXTHREAD 
X86_THREAD_STATE32      = 0x00000001
X86_THREAD_STATE64      = 0x00000004