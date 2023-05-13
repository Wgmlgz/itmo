 {addres: 0x01, encoded: 0x00A0009004,  decoded: "IP → BR, AR"}
 {addres: 0x02, encoded: 0x0104009420,  decoded: "BR + 1 → IP; MEM(AR) → DR"}
 {addres: 0x03, encoded: 0x0002009001,  decoded: "DR → CR"}
 {addres: 0x04, encoded: 0x8109804002,  decoded: "if CR(15) = 1 then GOTO CHKBR @ 09"}
 {addres: 0x05, encoded: 0x810C404002,  decoded: "if CR(14) = 1 then GOTO CHKABS @ 0C"}
 {addres: 0x06, encoded: 0x810C204002,  decoded: "if CR(13) = 1 then GOTO CHKABS @ 0C"}
 {addres: 0x07, encoded: 0x8078104002,  decoded: "if CR(12) = 0 then GOTO ADDRLESS @ 78"}
 {addres: 0x08, encoded: 0x80C2101040,  decoded: "GOTO IO @ C2"}
 {addres: 0x09, encoded: 0x800C404002,  decoded: "if CR(14) = 0 then GOTO CHKABS @ 0C"}
 {addres: 0x0A, encoded: 0x800C204002,  decoded: "if CR(13) = 0 then GOTO CHKABS @ 0C"}
 {addres: 0x0B, encoded: 0x8157104002,  decoded: "if CR(12) = 1 then GOTO BRANCHES @ 57"}
 {addres: 0x0C, encoded: 0x8024084002,  decoded: "if CR(11) = 0 then GOTO OPFETCH @ 24"}
 {addres: 0x0D, encoded: 0x0020011002,  decoded: "extend sign CR(0..7) → BR"}
 {addres: 0x0E, encoded: 0x811C044002,  decoded: "if CR(10) = 1 then GOTO T11XX @ 1C"}
 {addres: 0x0F, encoded: 0x0080009024,  decoded: "BR + IP → AR"}
 {addres: 0x10, encoded: 0x0100000000,  decoded: "MEM(AR) → DR"}
 {addres: 0x11, encoded: 0x8114024002,  decoded: "if CR(9) = 1 then GOTO T101X @ 14"}
 {addres: 0x12, encoded: 0x81E0014002,  decoded: "if CR(8) = 1 then GOTO RESERVED @ E0"}
 {addres: 0x13, encoded: 0x8024101040,  decoded: "GOTO OPFETCH @ 24"}
 {addres: 0x14, encoded: 0x8119014002,  decoded: "if CR(8) = 1 then GOTO T1011 @ 19"}
 {addres: 0x15, encoded: 0x0001009401,  decoded: "DR + 1 → DR"}
 {addres: 0x16, encoded: 0x0200000000,  decoded: "DR → MEM(AR)"}
 {addres: 0x17, encoded: 0x0001009201,  decoded: "~0 + DR → DR"}
 {addres: 0x18, encoded: 0x8024101040,  decoded: "GOTO OPFETCH @ 24"}
 {addres: 0x19, encoded: 0x0001009201,  decoded: "~0 + DR → DR"}
 {addres: 0x1A, encoded: 0x0200000000,  decoded: "DR → MEM(AR)"}
 {addres: 0x1B, encoded: 0x8024101040,  decoded: "GOTO OPFETCH @ 24"}
 {addres: 0x1C, encoded: 0x8120024002,  decoded: "if CR(9) = 1 then GOTO T111X @ 20"}
 {addres: 0x1D, encoded: 0x81E0014002,  decoded: "if CR(8) = 1 then GOTO RESERVED @ E0"}
 {addres: 0x1E, encoded: 0x0001009028,  decoded: "BR + SP → DR"}
 {addres: 0x1F, encoded: 0x8024101040,  decoded: "GOTO OPFETCH @ 24"}
 {addres: 0x20, encoded: 0x8023014002,  decoded: "if CR(8) = 0 then GOTO T1110 @ 23"}
 {addres: 0x21, encoded: 0x0001009020,  decoded: "BR → DR"}
 {addres: 0x22, encoded: 0x8028101040,  decoded: "GOTO EXEC @ 28"}
 {addres: 0x23, encoded: 0x0001009024,  decoded: "BR + IP → DR"}
 {addres: 0x24, encoded: 0x8026804002,  decoded: "if CR(15) = 0 then GOTO RDVALUE @ 26"}
 {addres: 0x25, encoded: 0x814A404002,  decoded: "if CR(14) = 1 then GOTO CMD11XX @ 4A"}
 {addres: 0x26, encoded: 0x0080009001,  decoded: "DR → AR"}
 {addres: 0x27, encoded: 0x0100000000,  decoded: "MEM(AR) → DR"}
 {addres: 0x28, encoded: 0x813C804002,  decoded: "if CR(15) = 1 then GOTO CMD1XXX @ 3C"}
 {addres: 0x29, encoded: 0x8130404002,  decoded: "if CR(14) = 1 then GOTO CMD01XX @ 30"}
 {addres: 0x2A, encoded: 0x812D104002,  decoded: "if CR(12) = 1 then GOTO OR @ 2D"}
 {addres: 0x2B, encoded: 0x0010C09811,  decoded: "AC & DR → AC, N, Z, V"}
 {addres: 0x2C, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x2D, encoded: 0x0020009B11,  decoded: "~AC & ~DR → BR"}
 {addres: 0x2E, encoded: 0x0010C09220,  decoded: "~BR → AC, N, Z, V"}
 {addres: 0x2F, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x30, encoded: 0x8137204002,  decoded: "if CR(13) = 1 then GOTO CMD011X @ 37"}
 {addres: 0x31, encoded: 0x8134104002,  decoded: "if CR(12) = 1 then GOTO ADC @ 34"}
 {addres: 0x32, encoded: 0x0010E09011,  decoded: "AC + DR → AC, N, Z, V, C"}
 {addres: 0x33, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x34, encoded: 0x8032011040,  decoded: "if PS(C) = 0 then GOTO ADD @ 32"}
 {addres: 0x35, encoded: 0x0010E09411,  decoded: "AC + DR + 1 → AC, N, Z, V, C"}
 {addres: 0x36, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x37, encoded: 0x813A104002,  decoded: "if CR(12) = 1 then GOTO CMP @ 3A"}
 {addres: 0x38, encoded: 0x0010E09511,  decoded: "AC + ~DR + 1 → AC, N, Z, V, C"}
 {addres: 0x39, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x3A, encoded: 0x0000E09511,  decoded: "AC + ~DR + 1 → N, Z, V, C"}
 {addres: 0x3B, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x3C, encoded: 0x8143204002,  decoded: "if CR(13) = 1 then GOTO CMD101X @ 43"}
 {addres: 0x3D, encoded: 0x81E0104002,  decoded: "if CR(12) = 1 then GOTO RESERVED @ E0"}
 {addres: 0x3E, encoded: 0x0001009201,  decoded: "~0 + DR → DR"}
 {addres: 0x3F, encoded: 0x0220009201,  decoded: "~0 + DR → BR; DR → MEM(AR)"}
 {addres: 0x40, encoded: 0x80C4804020,  decoded: "if BR(15) = 0 then GOTO INT @ C4"}
 {addres: 0x41, encoded: 0x0004009404,  decoded: "IP + 1 → IP"}
 {addres: 0x42, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x43, encoded: 0x8146104002,  decoded: "if CR(12) = 1 then GOTO SWAM @ 46"}
 {addres: 0x44, encoded: 0x0010C09001,  decoded: "DR → AC, N, Z, V"}
 {addres: 0x45, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x46, encoded: 0x0020009001,  decoded: "DR → BR"}
 {addres: 0x47, encoded: 0x0001009010,  decoded: "AC → DR"}
 {addres: 0x48, encoded: 0x0210C09020,  decoded: "BR → AC, N, Z, V; DR → MEM(AR)"}
 {addres: 0x49, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x4A, encoded: 0x8153204002,  decoded: "if CR(13) = 1 then GOTO ST @ 53"}
 {addres: 0x4B, encoded: 0x814E104002,  decoded: "if CR(12) = 1 then GOTO CALL @ 4E"}
 {addres: 0x4C, encoded: 0x0004009001,  decoded: "DR → IP"}
 {addres: 0x4D, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x4E, encoded: 0x0020009001,  decoded: "DR → BR"}
 {addres: 0x4F, encoded: 0x0001009004,  decoded: "IP → DR"}
 {addres: 0x50, encoded: 0x0004009020,  decoded: "BR → IP"}
 {addres: 0x51, encoded: 0x0088009208,  decoded: "~0 + SP → SP, AR"}
 {addres: 0x52, encoded: 0x8055101040,  decoded: "GOTO STORE @ 55"}
 {addres: 0x53, encoded: 0x0080009001,  decoded: "DR → AR"}
 {addres: 0x54, encoded: 0x0001009010,  decoded: "AC → DR"}
 {addres: 0x55, encoded: 0x0200000000,  decoded: "DR → MEM(AR)"}
 {addres: 0x56, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x57, encoded: 0x8171084002,  decoded: "if CR(11) = 1 then GOTO BR1XXX @ 71"}
 {addres: 0x58, encoded: 0x8166044002,  decoded: "if CR(10) = 1 then GOTO BR01XX @ 66"}
 {addres: 0x59, encoded: 0x8161024002,  decoded: "if CR(9) = 1 then GOTO BR001X @ 61"}
 {addres: 0x5A, encoded: 0x815F014002,  decoded: "if CR(8) = 1 then GOTO BNE @ 5F"}
 {addres: 0x5B, encoded: 0x80C4041040,  decoded: "if PS(Z) = 0 then GOTO INT @ C4"}
 {addres: 0x5C, encoded: 0x0020011002,  decoded: "extend sign CR(0..7) → BR"}
 {addres: 0x5D, encoded: 0x0004009024,  decoded: "BR + IP → IP"}
 {addres: 0x5E, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x5F, encoded: 0x805C041040,  decoded: "if PS(Z) = 0 then GOTO BR @ 5C"}
 {addres: 0x60, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x61, encoded: 0x8164014002,  decoded: "if CR(8) = 1 then GOTO BPL @ 64"}
 {addres: 0x62, encoded: 0x815C081040,  decoded: "if PS(N) = 1 then GOTO BR @ 5C"}
 {addres: 0x63, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x64, encoded: 0x805C081040,  decoded: "if PS(N) = 0 then GOTO BR @ 5C"}
 {addres: 0x65, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x66, encoded: 0x816C024002,  decoded: "if CR(9) = 1 then GOTO BR011X @ 6C"}
 {addres: 0x67, encoded: 0x816A014002,  decoded: "if CR(8) = 1 then GOTO BCC @ 6A"}
 {addres: 0x68, encoded: 0x815C011040,  decoded: "if PS(C) = 1 then GOTO BR @ 5C"}
 {addres: 0x69, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x6A, encoded: 0x805C011040,  decoded: "if PS(C) = 0 then GOTO BR @ 5C"}
 {addres: 0x6B, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x6C, encoded: 0x816F014002,  decoded: "if CR(8) = 1 then GOTO BVC @ 6F"}
 {addres: 0x6D, encoded: 0x815C021040,  decoded: "if PS(V) = 1 then GOTO BR @ 5C"}
 {addres: 0x6E, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x6F, encoded: 0x805C021040,  decoded: "if PS(V) = 0 then GOTO BR @ 5C"}
 {addres: 0x70, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x71, encoded: 0x81E0044002,  decoded: "if CR(10) = 1 then GOTO RESERVED @ E0"}
 {addres: 0x72, encoded: 0x81E0024002,  decoded: "if CR(9) = 1 then GOTO RESERVED @ E0"}
 {addres: 0x73, encoded: 0x8176014002,  decoded: "if CR(8) = 1 then GOTO BGE @ 76"}
 {addres: 0x74, encoded: 0x806D081040,  decoded: "if PS(N) = 0 then GOTO BVS @ 6D"}
 {addres: 0x75, encoded: 0x806F101040,  decoded: "GOTO BVC @ 6F"}
 {addres: 0x76, encoded: 0x806F081040,  decoded: "if PS(N) = 0 then GOTO BVC @ 6F"}
 {addres: 0x77, encoded: 0x806D101040,  decoded: "GOTO BVS @ 6D"}
 {addres: 0x78, encoded: 0x81A4084002,  decoded: "if CR(11) = 1 then GOTO AL1XXX @ A4"}
 {addres: 0x79, encoded: 0x8189044002,  decoded: "if CR(10) = 1 then GOTO AL01XX @ 89"}
 {addres: 0x7A, encoded: 0x817D024002,  decoded: "if CR(9) = 1 then GOTO AL001X @ 7D"}
 {addres: 0x7B, encoded: 0x80C4014002,  decoded: "if CR(8) = 0 then GOTO INT @ C4"}
 {addres: 0x7C, encoded: 0x80DE101040,  decoded: "GOTO STOP @ DE"}
 {addres: 0x7D, encoded: 0x8183014002,  decoded: "if CR(8) = 1 then GOTO AL0011 @ 83"}
 {addres: 0x7E, encoded: 0x8181801002,  decoded: "if CR(7) = 1 then GOTO CMA @ 81"}
 {addres: 0x7F, encoded: 0x0010C00000,  decoded: "0 → AC, N, Z, V"}
 {addres: 0x80, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x81, encoded: 0x0010C09210,  decoded: "~AC → AC, N, Z, V"}
 {addres: 0x82, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x83, encoded: 0x8186801002,  decoded: "if CR(7) = 1 then GOTO CMC @ 86"}
 {addres: 0x84, encoded: 0x0000200000,  decoded: "0 → C"}
 {addres: 0x85, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x86, encoded: 0x8184011040,  decoded: "if PS(C) = 1 then GOTO CLC @ 84"}
 {addres: 0x87, encoded: 0x0000208300,  decoded: "HTOH(~0 + ~0) → C"}
 {addres: 0x88, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x89, encoded: 0x8196024002,  decoded: "if CR(9) = 1 then GOTO AL011X @ 96"}
 {addres: 0x8A, encoded: 0x8190014002,  decoded: "if CR(8) = 1 then GOTO AL0101 @ 90"}
 {addres: 0x8B, encoded: 0x818E801002,  decoded: "if CR(7) = 1 then GOTO ROR @ 8E"}
 {addres: 0x8C, encoded: 0x0010E60010,  decoded: "ROL(AC) → AC, N, Z, V, C"}
 {addres: 0x8D, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x8E, encoded: 0x0010F80010,  decoded: "ROR(AC) → AC, N, Z, V, C"}
 {addres: 0x8F, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x90, encoded: 0x8194801002,  decoded: "if CR(7) = 1 then GOTO ASR @ 94"}
 {addres: 0x91, encoded: 0x0001009010,  decoded: "AC → DR"}
 {addres: 0x92, encoded: 0x0010E09011,  decoded: "AC + DR → AC, N, Z, V, C"}
 {addres: 0x93, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x94, encoded: 0x0010E80010,  decoded: "ASR(AC) → AC, N, Z, V, C"}
 {addres: 0x95, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x96, encoded: 0x819C014002,  decoded: "if CR(8) = 1 then GOTO AL0111 @ 9C"}
 {addres: 0x97, encoded: 0x819A801002,  decoded: "if CR(7) = 1 then GOTO SWAB @ 9A"}
 {addres: 0x98, encoded: 0x0010C11010,  decoded: "extend sign AC(0..7) → AC, N, Z, V"}
 {addres: 0x99, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x9A, encoded: 0x0010C06010,  decoded: "SWAB(AC) → AC, N, Z, V"}
 {addres: 0x9B, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0x9C, encoded: 0x81A2801002,  decoded: "if CR(7) = 1 then GOTO NEG @ A2"}
 {addres: 0x9D, encoded: 0x81A0401002,  decoded: "if CR(6) = 1 then GOTO DEC @ A0"}
 {addres: 0x9E, encoded: 0x0010E09410,  decoded: "AC + 1 → AC, N, Z, V, C"}
 {addres: 0x9F, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0xA0, encoded: 0x0010E09110,  decoded: "AC + ~0 → AC, N, Z, V, C"}
 {addres: 0xA1, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0xA2, encoded: 0x0010E09610,  decoded: "~AC + 1 → AC, N, Z, V, C"}
 {addres: 0xA3, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0xA4, encoded: 0x81B5044002,  decoded: "if CR(10) = 1 then GOTO AL11XX @ B5"}
 {addres: 0xA5, encoded: 0x0080009008,  decoded: "SP → AR"}
 {addres: 0xA6, encoded: 0x0100000000,  decoded: "MEM(AR) → DR"}
 {addres: 0xA7, encoded: 0x81AE024002,  decoded: "if CR(9) = 1 then GOTO AL101X @ AE"}
 {addres: 0xA8, encoded: 0x81AC014002,  decoded: "if CR(8) = 1 then GOTO POPF @ AC"}
 {addres: 0xA9, encoded: 0x0010C09001,  decoded: "DR → AC, N, Z, V"}
 {addres: 0xAA, encoded: 0x0008009408,  decoded: "SP + 1 → SP"}
 {addres: 0xAB, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0xAC, encoded: 0x0040009001,  decoded: "DR → PS"}
 {addres: 0xAE, encoded: 0x81B1014002,  decoded: "if CR(8) = 1 then GOTO IRET @ B1"}
 {addres: 0xAF, encoded: 0x0004009001,  decoded: "DR → IP"}
 {addres: 0xB0, encoded: 0x80AA101040,  decoded: "GOTO INCSP @ AA"}
 {addres: 0xB1, encoded: 0x0040009001,  decoded: "DR → PS"}
 {addres: 0xB2, encoded: 0x0088009408,  decoded: "SP + 1 → SP, AR"}
 {addres: 0xB3, encoded: 0x0100000000,  decoded: "MEM(AR) → DR"}
 {addres: 0xB4, encoded: 0x80AF101040,  decoded: "GOTO RET @ AF"}
 {addres: 0xB5, encoded: 0x81BB024002,  decoded: "if CR(9) = 1 then GOTO AL111X @ BB"}
 {addres: 0xB6, encoded: 0x81B9014002,  decoded: "if CR(8) = 1 then GOTO PUSHF @ B9"}
 {addres: 0xB7, encoded: 0x0001009010,  decoded: "AC → DR"}
 {addres: 0xB8, encoded: 0x8051101040,  decoded: "GOTO PUSHVAL @ 51"}
 {addres: 0xB9, encoded: 0x0001009040,  decoded: "PS → DR"}
 {addres: 0xBA, encoded: 0x8051101040,  decoded: "GOTO PUSHVAL @ 51"}
 {addres: 0xBB, encoded: 0x81E0014002,  decoded: "if CR(8) = 1 then GOTO RESERVED @ E0"}
 {addres: 0xBC, encoded: 0x0080009008,  decoded: "SP → AR"}
 {addres: 0xBD, encoded: 0x0100000000,  decoded: "MEM(AR) → DR"}
 {addres: 0xBE, encoded: 0x0020009001,  decoded: "DR → BR"}
 {addres: 0xBF, encoded: 0x0001009010,  decoded: "AC → DR"}
 {addres: 0xC0, encoded: 0x0210C09020,  decoded: "BR → AC, N, Z, V; DR → MEM(AR)"}
 {addres: 0xC1, encoded: 0x80C4101040,  decoded: "GOTO INT @ C4"}
 {addres: 0xC2, encoded: 0x81C7084002,  decoded: "if CR(11) = 1 then GOTO IRQ @ C7"}
 {addres: 0xC3, encoded: 0x0400000000,  decoded: "IO"}
 {addres: 0xC4, encoded: 0x80DE801040,  decoded: "if PS(W) = 0 then GOTO STOP @ DE"}
 {addres: 0xC5, encoded: 0x8001401040,  decoded: "if PS(IRQ) = 0 then GOTO INFETCH @ 01"}
 {addres: 0xC6, encoded: 0x0800000000,  decoded: "IRQSC"}
 {addres: 0xC7, encoded: 0x0088009208,  decoded: "~0 + SP → SP, AR"}
 {addres: 0xC8, encoded: 0x0001009004,  decoded: "IP → DR"}
 {addres: 0xC9, encoded: 0x0200000000,  decoded: "DR → MEM(AR)"}
 {addres: 0xCA, encoded: 0x0088009208,  decoded: "~0 + SP → SP, AR"}
 {addres: 0xCB, encoded: 0x0001009040,  decoded: "PS → DR"}
 {addres: 0xCC, encoded: 0x0220001002,  decoded: "LTOL(CR) → BR; DR → MEM(AR)"}
 {addres: 0xCD, encoded: 0x00A0020020,  decoded: "SHL(BR) → BR, AR"}
 {addres: 0xCE, encoded: 0x0100000000,  decoded: "MEM(AR) → DR"}
 {addres: 0xCF, encoded: 0x0004009001,  decoded: "DR → IP"}
 {addres: 0xD0, encoded: 0x0080001420,  decoded: "LTOL(BR + 1) → AR"}
 {addres: 0xD1, encoded: 0x0100000000,  decoded: "MEM(AR) → DR"}
 {addres: 0xD2, encoded: 0x0040009001,  decoded: "DR → PS"}
 {addres: 0xD3, encoded: 0x8001101040,  decoded: "GOTO INFETCH @ 01"}
 {addres: 0xD4, encoded: 0x00BBE00000,  decoded: "0 → DR, CR, SP, AC, BR, AR, N, Z, V, C"}
 {addres: 0xD5, encoded: 0x80C3101040,  decoded: "GOTO DOIO @ C3"}
 {addres: 0xD6, encoded: 0x0080009004,  decoded: "IP → AR"}
 {addres: 0xD7, encoded: 0x0104009404,  decoded: "IP + 1 → IP; MEM(AR) → DR"}
 {addres: 0xD8, encoded: 0x80DE101040,  decoded: "GOTO STOP @ DE"}
 {addres: 0xD9, encoded: 0x0080009004,  decoded: "IP → AR"}
 {addres: 0xDA, encoded: 0x0001009080,  decoded: "IR → DR"}
 {addres: 0xDB, encoded: 0x0204009404,  decoded: "IP + 1 → IP; DR → MEM(AR)"}
 {addres: 0xDC, encoded: 0x80DE101040,  decoded: "GOTO STOP @ DE"}
 {addres: 0xDD, encoded: 0x0004009080,  decoded: "IR → IP"}
 {addres: 0xDE, encoded: 0x4000000000,  decoded: "Halt"}