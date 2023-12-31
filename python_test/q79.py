import multiprocessing
def sum_worker(data_chunk):
    return sum(data_chunk)
def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 100000
    pool = multiprocessing.Pool(processes=4)
    chunksize = len(data) // 4
    chunks = [data[i:i+chunksize] for i in range(0, len(data), chunksize)]
    results = pool.map(sum_worker, chunks)
    pool.close()
    pool.join()
    total = sum(results)
    print(total)
if __name__ == "__main__":
    main()