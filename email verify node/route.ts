import { NextResponse } from "next/server";
import {getCode, deleteCode } from "@/lib/codes";
import * as cookie from "cookie";

const codes = new Map(); // Store codes temporarily (Use DB for production)

export async function POST(req: Request) {
  const { email, code } = await req.json();

  const storedCode = getCode(email); // Retrieve the code for the email

  if (storedCode == code) {
    deleteCode(email); // Remove code after successful verification
    return NextResponse.json({ message: "Code verified!" });
  }

  return NextResponse.json({ message: "Invalid code!" }, { status: 400 });


}

