import { Company } from './company.model';

export interface Item {
  id: number;
  title: string;
  imageUrl: string;
  price: number;
  investorNumber: number;
  investAmount: number;
  companyInfo: Company;
  description: string;
}
