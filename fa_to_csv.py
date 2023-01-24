#!/usr/bin/python3
from Bio import SeqIO
import argparse
import csv


def fasta_to_csv(fa, out_csv, seq_id, seq):
    with open(out_csv, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([seq_id, seq])
        for record in SeqIO.parse(fa, "fasta"):
            writer.writerow([record.id, record.seq])


def main():  
    args = arguments()
    fasta_to_csv(args.i_fa, args.o_csv, args.id, args.seq)


def arguments():
    parser = argparse.ArgumentParser(description="Converts fasta to csv.")
    parser.add_argument('--i_fa', help="Name of input fasta file", type=str,
                        required=True)
    parser.add_argument('--o_csv', help="Output file in csv format", type=str,
                        required=True)
    parser.add_argument('--id', help="Name of id column",
                        type=str, default="sequence_id")
    parser.add_argument('--seq', help="Name of sequence column",
                        type=str, default="sequence")
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    main()
