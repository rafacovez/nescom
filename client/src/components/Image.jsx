export default function Image({ src, alt }) {
  return (
    <img src={src} alt={alt} loading='lazy' style={{ maxWidth: '100%' }} />
  );
}
