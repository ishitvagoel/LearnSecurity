import { NextResponse } from "next/server";
import { buildSearchIndex } from "@/lib/searchIndex";

export const dynamic = "force-static";

export function GET() {
  return NextResponse.json(buildSearchIndex());
}
