// lib/codes.ts
const codes = new Map<string, string>(); // Temporary in-memory storage

export function setCode(email:string,code:string) {
  codes.set(email, code);
}

export function getCode(email:string) {
  return codes.get(email);
}

export function deleteCode(email:string) {
  codes.delete(email);
}

export default codes;
