import { Company } from './company.model';

interface Yield {
  name: string;
  수익률: number;
}
export interface Item {
  id: number;
  title: string;
  imageUrl: string;
  price: number;
  investorNumber: number;
  investAmount: number;
  companyInfo: Company;
  description: string;
  yield: Yield[];
  totalFund: number;
  profitPercent: number;
  fundingPercent: number;
}
