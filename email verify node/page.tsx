"use client";
import { useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from 'next/link';

const VerifyCode = () => {
  const searchParams = useSearchParams();
  const email = searchParams.get("email") || "";
  const [code, setCode] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const res = await fetch("/api/verifyCode", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, code }),
    });

    const data = await res.json();

    if (res.ok) {
      router.push("/resume");
    } else {
      setError("Invalid code! Try again.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col">
    {/* Navigation */}
      <nav className="flex justify-between items-center p-5 w-full bg-gray-800 fixed top-0 left-0 z-10">
        <Link href="/" className="text-white">Home</Link>
        <div className="flex gap-4 text-white">
          <Link href="/contact">Contact</Link>
          <Link href="/about">About Me</Link>
          <Link href="/resume">Resume</Link>
          <Link href="/projects">Projects</Link>
        </div>
      </nav>
    

    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="p-8 bg-white rounded shadow-md">
        <h1 className="text-2xl font-bold mb-4">Enter Verification Code</h1>
        <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
          <input
            type="text"
            placeholder="Enter Code"
            value={code}
            onChange={(e) => setCode(e.target.value)}
            className="p-2 border rounded"
            required
          />
          <button
            type="submit"
            className="bg-blue-500 text-white p-2 rounded hover:bg-blue-700"
          >
            Verify Code
          </button>
          {error && <p className="text-red-500">{error}</p>}
        </form>
      </div>
    </div>
  </div>
  );
};

export default VerifyCode;
