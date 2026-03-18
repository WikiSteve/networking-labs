# LAB Component Search

- Filename: `LAB Component Search.docx`
- Subject: `systems`
- Type: `lab`
- Reusable: `yes`
- Source file: [Source copy](../../sources/LAB%20Component%20Search.docx)

## Summary

This reusable in-person hardware and BIOS inspection lab functions as a practical attendance, participation, and peer-check activity. It has three required sections: clearing, setting, and removing a BIOS password using both motherboard jumper and BIOS menu methods; performing a BIOS scavenger hunt to locate system configuration details such as BIOS version, CPU, RAM, boot order, TPM, virtualization, Secure Boot, PXE, and password status; and physically identifying installed hardware components such as CPU type, RAM generation, storage type, SATA versus NVMe, power supply wattage, fan count, USB ports, and PCIe slots. It is strongly hands-on and verification-driven, with instructor checkoffs and required peer sign-off before students leave.

## Key Details

- Section 1 focuses on BIOS password handling, including clearing an existing password using the motherboard PSWD jumper.
- The jumper procedure explicitly moves the 2-pin jumper from pins 2-3 to pins 1-2, boots to POST, powers off, and restores the jumper.
- After clearing the old password, the learner boots into BIOS with `F2`, sets a Supervisor or System password, and then removes it.
- Each password stage requires instructor verification.
- Section 2 is a BIOS scavenger hunt that requires locating and recording firmware settings and system information.
- BIOS items include BIOS version and date, CPU model and speed, RAM total, boot sequence, TPM status, virtualization status, Secure Boot status, date and time, PXE visibility, and supervisor-password status.
- After BIOS approval, each learner must check another person's answers and initial that sheet.
- Section 3 shifts to physical hardware identification by direct inspection of the machine.
- Required component details include CPU vendor and socket or model, RAM type, number of RAM sticks, storage type, SATA versus NVMe, power supply wattage, fan count, USB port count, and visible PCIe slots.
- A peer sign-off sheet is included with spaces for initials and completion time.
- The rules state that all three sections must be completed to be marked present.

## Tags

- `bios`
- `hardware-identification`
- `firmware`
- `jumper-reset`
- `pc-components`
- `peer-checkoff`
- `lab`
- `attendance-practical`
