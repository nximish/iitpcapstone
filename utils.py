import time
import logging

def invoke_with_retry(chain, inputs, max_retries = 3, delay = 2):
    # tries chain.invoke() up to max_retries times, backs off between attempts
    for attempt in range(1, max_retries + 1):
        try:
            return chain.invoke(inputs)
        except Exception as e:
            logging.info(f"LLM call failed (attempt {attempt}/{max_retries}): {e}")
            if attempt == max_retries:
                raise
            time.sleep(delay * attempt)