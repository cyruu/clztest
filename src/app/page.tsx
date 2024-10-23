"use client";
import axios from "axios";
import { useState } from "react";

export default function Home() {
  const [sentence, setSentence] = useState("");
  const [sentiment, setSentiment] = useState(null);
  const [loading, setLoading] = useState(false);
  async function handleSubmit(e: any) {
    e.preventDefault();
    setLoading(true);
    const { data } = await axios.post("http://localhost:8001/calcsentiment", {
      sentence: sentence,
    });
    setSentiment(data.sentiment);
    setLoading(false);
  }
  return (
    <>
      <form onSubmit={handleSubmit}>
        <input
          className="border border-2"
          type="text"
          value={sentence}
          onChange={({ target }) => setSentence(target.value)}
        />
        <button type="submit">Analyze</button>
      </form>
      {loading ? <p>Analyzing...</p> : ""}
      {sentiment ? (
        <p
          className={
            sentiment == "Positive"
              ? "bg-green-500"
              : sentiment == "Negative"
              ? "bg-red-500"
              : "bg-white"
          }
        >
          {sentiment}
        </p>
      ) : (
        ""
      )}
    </>
  );
}
