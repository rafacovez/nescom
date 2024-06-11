import MainLayout from '../layouts/MainLayout';
import useDocumentTitle from '../functions/useDocumentTitle';

export default function NotFound() {
  useDocumentTitle('Not found');

  return <MainLayout>This page was not found</MainLayout>;
}
